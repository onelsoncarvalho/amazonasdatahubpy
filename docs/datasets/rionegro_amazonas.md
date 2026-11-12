---
file_format: mystnb
kernelspec:
  name: python3
  display_name: Python 3
  language: python
---

% ARQUIVO GERADO por docs/conf.py. Não edite aqui: edite ../../src/amazonasdatahub/documentations/rionegro_amazonas.md


```{include} ../../src/amazonasdatahub/documentations/rionegro_amazonas.md
:relative-images:
:start-line: 3
:end-line: 50
```

### Example

```{code-cell} python
import matplotlib.pyplot as plt
from amazonasdatahub.datasets import get_dataset

# Load dataset
rionegro_amazonas = get_dataset("rionegro_amazonas")

# Prepare data for boxplot grouped by year
years = sorted(rionegro_amazonas["year"].unique())
data_by_year = [
    rionegro_amazonas[rionegro_amazonas["year"] == yr]["level_m"].dropna()
    for yr in years
]

# Plot boxplot
fig, ax = plt.subplots(figsize=(10, 5))
ax.boxplot(data_by_year, tick_labels=years)

# Labels
ax.set_xlabel("Year")
ax.set_ylabel("Water level (m)")

plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
```
