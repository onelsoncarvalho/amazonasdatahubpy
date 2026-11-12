---
file_format: mystnb
kernelspec:
  name: python3
  display_name: Python 3
  language: python
---

% ARQUIVO GERADO por docs/conf.py. Não edite aqui: edite ../../src/amazonasdatahub/documentations/prf_amazonas.md


```{include} ../../src/amazonasdatahub/documentations/prf_amazonas.md
:relative-images:
:start-line: 3
:end-line: 138
```

### Example

```{code-cell} python
import matplotlib.pyplot as plt
from amazonasdatahub.datasets import get_dataset

# Load dataset
prf_amazonas = get_dataset("prf_amazonas")

# Count occurrences by weather condition (automatically sorted descending)
counts = prf_amazonas["weather"].value_counts()

# Plot bar chart
fig, ax = plt.subplots(figsize=(9, 6))
bars = ax.bar(counts.index, counts.values, color="steelblue", edgecolor="gray")

# Add text labels on top of bars
ax.bar_label(bars, padding=3)

# Titles and labels
ax.set_title("Accident count by weather condition", loc="left")
ax.set_xlabel("Weather")
ax.set_ylabel("Count")

plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
```
