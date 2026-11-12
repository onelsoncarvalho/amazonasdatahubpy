---
file_format: mystnb
kernelspec:
  name: python3
  display_name: Python 3
  language: python
---

% ARQUIVO GERADO por docs/conf.py. Não edite aqui: edite ../../src/amazonasdatahub/documentations/humidity_manaus.md


```{include} ../../src/amazonasdatahub/documentations/humidity_manaus.md
:relative-images:
:start-line: 3
:end-line: 48
```

### Example

```{code-cell} python
import matplotlib.pyplot as plt
import pandas as pd
from amazonasdatahub.datasets import get_dataset

# Load dataset
humidity_manaus = get_dataset("humidity_manaus")

# Create date column from year and month
humidity_manaus["date"] = pd.to_datetime(
    humidity_manaus["year"].astype(str)
    + "-"
    + humidity_manaus["month"].astype(str)
    + "-01"
)

# Sort by date for proper line plotting
humidity_manaus = humidity_manaus.sort_values("date")

# Plot time series
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(
    humidity_manaus["date"], humidity_manaus["rh"], color="tab:blue", lw=1.5
)

# Titles and labels
ax.set_title("Relative Humidity of Amazonas (2010 - 2020)")
ax.set_xlabel("Date")
ax.set_ylabel("Relative Humidity")

plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
```
