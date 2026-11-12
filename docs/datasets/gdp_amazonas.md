---
file_format: mystnb
kernelspec:
  name: python3
  display_name: Python 3
  language: python
---

% ARQUIVO GERADO por docs/conf.py. Não edite aqui: edite ../../src/amazonasdatahub/documentations/gdp_amazonas.md


```{include} ../../src/amazonasdatahub/documentations/gdp_amazonas.md
:relative-images:
:start-line: 3
:end-line: 103
```

### Example

```{code-cell} python
import matplotlib.pyplot as plt
from amazonasdatahub.datasets import get_dataset

# Load dataset
gdp_amazonas = get_dataset("gdp_amazonas")

# Select only year and taxes
df_gdp = gdp_amazonas[["year", "taxes"]]

# Plot time series
plt.figure(figsize=(9, 5))
plt.plot(
    df_gdp["year"],
    df_gdp["taxes"],
    color="#cb181d",
    linewidth=2,
)

# Add horizontal dashed line for the mean of taxes
mean_taxes = df_gdp["taxes"].mean()
plt.axhline(
    y=mean_taxes,
    color="gray",
    linestyle="--",
    linewidth=1.5,
)

# Information - Title, subtitle and style
plt.title(
    "Quarterly GDP of Amazonas (2010-2021)", fontweight="bold", fontsize=14, loc="left"
)
plt.xlabel("Year")
plt.ylabel("Taxes")

plt.grid(True, linestyle=":", alpha=0.6)
plt.tight_layout()
plt.show()
```
