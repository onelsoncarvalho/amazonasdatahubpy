import sys
import types

import pytest

from amazonasdatahub import docs


@pytest.fixture
def docs_dir(tmp_path, monkeypatch):
    monkeypatch.setattr(docs.resources, "files", lambda package: tmp_path)
    return tmp_path


def test_doc_not_found(docs_dir, capsys):
    docs.get_doc("missing")

    assert "Docs for missing not found" in capsys.readouterr().out


def test_prints_body_without_ipython(docs_dir, monkeypatch, capsys):
    (docs_dir / "sample.md").write_text(
        "---\ntitle: Sample Title\n---\n\nBody text", encoding="utf-8"
    )
    monkeypatch.setitem(sys.modules, "IPython.display", None)  # forces ImportError

    docs.get_doc("sample")

    out = capsys.readouterr().out
    assert "Documentation from: Sample Title" in out
    assert "Body text" in out


def test_displays_markdown_with_ipython(docs_dir, monkeypatch):
    (docs_dir / "sample.md").write_text(
        "---\ntitle: Sample Title\n---\n\nBody text", encoding="utf-8"
    )
    displayed = []
    fake = types.ModuleType("IPython.display")
    fake.display = displayed.append
    fake.Markdown = lambda text: ("markdown", text)
    monkeypatch.setitem(sys.modules, "IPython.display", fake)

    docs.get_doc("sample")

    assert displayed == [("markdown", "Body text")]


def test_title_defaults_to_uppercase_name(docs_dir, monkeypatch, capsys):
    (docs_dir / "sample.md").write_text("Just a body", encoding="utf-8")
    monkeypatch.setitem(sys.modules, "IPython.display", None)

    docs.get_doc("sample")

    assert "Documentation from: SAMPLE" in capsys.readouterr().out


def test_error_is_reported(monkeypatch, capsys):
    def boom(package):
        raise RuntimeError("broken")

    monkeypatch.setattr(docs.resources, "files", boom)

    docs.get_doc("sample")

    assert "Error while processing docs: broken" in capsys.readouterr().out
