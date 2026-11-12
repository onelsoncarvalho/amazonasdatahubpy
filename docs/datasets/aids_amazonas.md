---
file_format: mystnb
kernelspec:
  name: python3
  display_name: Python 3
  language: python
---

% ARQUIVO GERADO por docs/conf.py. Não edite aqui: edite ../../src/amazonasdatahub/documentations/aids_amazonas.md


```{include} ../../src/amazonasdatahub/documentations/aids_amazonas.md
:relative-images:
:start-line: 3
:end-line: 48
```

### Example

```{code-cell} python
import matplotlib.pyplot as plt
from amazonasdatahub.datasets import get_dataset

# Load dataset
aids_amazonas = get_dataset("aids_amazonas")

# Filter by municipality and pivot data by gender
manaus_aids = aids_amazonas[aids_amazonas["name_muni"] == "Manaus"]
pivot_aids = manaus_aids.pivot(
    index="year", columns="gender", values="cases"
)

# Plot line chart
pivot_aids.plot(marker="o", figsize=(9, 5))

# Titles, labels and custom configurations
plt.title("AIDS occurrences in Manaus (2011-2023)")
plt.xlabel("Year")
plt.ylabel("Case count")
plt.legend(title="Gender")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
```
