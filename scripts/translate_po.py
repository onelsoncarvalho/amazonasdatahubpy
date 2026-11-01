# scripts/translate_po.py
import os
import pathlib
import re
from xml.sax.saxutils import escape, unescape

import deepl
import polib

LOCALE_DIR = pathlib.Path("docs/locales/pt_BR")
BATCH = 40
RESERVE = 20_000   # margem de segurança sobre a cota mensal

# Termos que nunca devem ser traduzidos (edite à vontade)
NO_TRANSLATE = ["amazonasdatahub", "AmazonasDataHub", "IDAM", "IBGE", "pip", "wheel", "CLI", "API"]

# Termos que devem sobreviver intactos à tradução
TERMS = re.compile(
    r"\b[A-Za-z0-9]+(?:_[A-Za-z0-9]+)+\b"                      # identificadores: agriculture_amazonas
    r"|\b(?:" + "|".join(map(re.escape, NO_TRANSLATE)) + r")\b"
)

# O que fica intacto. A ordem importa: padrões mais longos primeiro.
PROTECT = re.compile("|".join([
    r"\{[\w:.+-]+\}`[^`]*`",          # role MyST: {ref}`...`
    r":[\w:.+-]+:`[^`]*`",            # role RST:  :ref:`...`
    r"``[^`]+``",                     # código inline RST
    r"`[^`]+`_{0,2}",                 # código inline Markdown / links RST
    r"\]\([^)]*\)",                   # destino de link/imagem Markdown: ](url)
    r"<https?://[^>\s]+>",            # autolink
    r"https?://[^\s<>)]+",            # URL solta
    r"%\(\w+\)[sd]",                  # placeholders Python
    r"\{[^{}\s]*\}",                  # {placeholders}
    TERMS.pattern,
]))

# Imagem Markdown com caminho relativo: não traduzir
SKIP = re.compile(r"!\[[^\]]*\]\((?!https?://)[^)]*\)")
TAG = re.compile(r'<x i="(\d+)"\s*(?:/>|>\s*</x>)')


def protect(text):
    spans, out, last = [], [], 0
    for m in PROTECT.finditer(text):
        out.append(escape(text[last:m.start()]))
        out.append(f'<x i="{len(spans)}"/>')
        spans.append(m.group(0))
        last = m.end()
    out.append(escape(text[last:]))
    return "".join(out), spans


def restore(translated, spans):
    """Devolve a marcação original. Retorna None se alguma tag sumiu/duplicou."""
    parts = TAG.split(translated)          # [texto, id, texto, id, ...]
    used, out = [], []
    for k, part in enumerate(parts):
        if k % 2 == 0:
            out.append(unescape(part))
        else:
            i = int(part)
            if i >= len(spans):
                return None
            used.append(i)
            out.append(spans[i])
    if sorted(used) != list(range(len(spans))):
        return None
    return "".join(out)


def needs(e):
    return (not e.obsolete and not SKIP.search(e.msgid)
            and (not e.msgstr or "fuzzy" in e.flags))


def mark_done(e, text):
    e.msgstr = text
    if "fuzzy" in e.flags:
        e.flags.remove("fuzzy")


client = deepl.DeepLClient(os.environ["DEEPL_API_KEY"])

try:
    usage = client.get_usage().character
    budget = usage.limit - usage.count - RESERVE
except Exception:
    budget = 300_000
print(f"Orçamento de caracteres neste run: {budget}")

pos = {p: polib.pofile(str(p)) for p in LOCALE_DIR.rglob("*.po")}

# Correção automática: apaga traduções que perderam um termo protegido
# e traduções de strings com imagem relativa (serão retraduzidas ou ignoradas)
for po in pos.values():
    for e in po:
        if e.obsolete or "fuzzy" in e.flags or not e.msgstr:
            continue
        terms = [m.group(0) for m in TERMS.finditer(e.msgid)]
        if SKIP.search(e.msgid) or any(t not in e.msgstr for t in terms):
            e.msgstr = ""

# Memória de tradução: tudo que já está traduzido (inclui correções manuais)
memory = {
    e.msgid: e.msgstr
    for po in pos.values() for e in po
    if e.msgstr and "fuzzy" not in e.flags and not e.obsolete
}

# Strings sem texto traduzível (números, símbolos, só termos protegidos)
# não precisam de tradução nem gastam cota
for po in pos.values():
    for e in po:
        if needs(e) and not re.search(r"[A-Za-z]", PROTECT.sub("", e.msgid)):
            memory.setdefault(e.msgid, e.msgid)

pending = sorted({e.msgid for po in pos.values() for e in po
                  if needs(e) and e.msgid not in memory})
print(f"{len(pending)} strings para traduzir")

translated_count = 0
for i in range(0, len(pending), BATCH):
    chunk = pending[i:i + BATCH]
    prepared = [protect(s) for s in chunk]
    cost = sum(len(p[0]) for p in prepared)
    if cost > budget:
        print("Cota mensal quase no fim; o restante fica para o próximo run.")
        break
    try:
        results = client.translate_text(
            [p[0] for p in prepared],
            source_lang="EN",
            target_lang="PT-BR",
            tag_handling="xml",
            non_splitting_tags=["x"],
            split_sentences="nonewlines",
            preserve_formatting=True,
        )
    except deepl.QuotaExceededException:
        print("Cota do DeepL esgotada; o restante fica para o próximo run.")
        break
    budget -= cost
    for src, (_, spans), res in zip(chunk, prepared, results):
        restored = restore(res.text, spans)
        if restored is not None:
            memory[src] = restored
            translated_count += 1
        else:
            print(f"Marcação quebrada, ignorada: {src[:60]!r}")

# Aplica a memória em todos os catálogos
for path, po in pos.items():
    for e in po:
        if needs(e) and e.msgid in memory:
            mark_done(e, memory[e.msgid])
    po.save()

print(f"{translated_count} strings traduzidas")
