---
file_format: mystnb
kernelspec:
  name: python3
  display_name: Python 3
  language: python
---

% ARQUIVO GERADO por docs/conf.py. Não edite aqui: edite ../../src/amazonasdatahub/documentations/agriculture_amazonas.md


```{include} ../../src/amazonasdatahub/documentations/agriculture_amazonas.md
:relative-images:
:start-line: 3
:end-line: 80
```

### Example

```{code-cell} python
import matplotlib.pyplot as plt
from amazonasdatahub.datasets import get_dataset

# Loading data
agriculture_amazonas = get_dataset("agriculture_amazonas")

# Filtering data
mandioca_prod = agriculture_amazonas[
  agriculture_amazonas["cultivation"] == "Mandioca"
]

# Scatterplot
plt.figure(figsize=(8,6))
plt.scatter(
  mandioca_prod["planted"],
  mandioca_prod["harvested"],
  alpha=0.7,
  edgecolors="none"
)
plt.xlabel("Planted area (hectare)")
plt.ylabel("Harvested area (hectare)")
plt.title("Cassava production in Amazonas")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
```
