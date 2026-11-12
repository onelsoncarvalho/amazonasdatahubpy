---
file_format: mystnb
kernelspec:
  name: python3
  display_name: Python 3
  language: python
---

% ARQUIVO GERADO por docs/conf.py. Não edite aqui: edite ../../src/amazonasdatahub/documentations/srl_muni.md


```{include} ../../src/amazonasdatahub/documentations/srl_muni.md
:relative-images:
:start-line: 3
:end-line: 94
```

### Example

```{code-cell} python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from amazonasdatahub.datasets import get_dataset

srl_muni = get_dataset("srl_muni")

# Selecting numeric variables and computing the correlation matrix
corr = srl_muni.select_dtypes("number").corr()
labels = corr.columns

# Plotting the correlation matrix
cmap = LinearSegmentedColormap.from_list("corr", ["#2166AC", "white", "#d50e0b"])

fig, ax = plt.subplots(figsize=(8, 8))
im = ax.imshow(corr.values, cmap=cmap, vmin=-1, vmax=1)

ax.set_xticks(np.arange(len(labels)), labels=labels, rotation=45, ha="right")
ax.set_yticks(np.arange(len(labels)), labels=labels)

# Cell borders and value labels
ax.set_xticks(np.arange(-0.5, len(labels), 1), minor=True)
ax.set_yticks(np.arange(-0.5, len(labels), 1), minor=True)
ax.grid(which="minor", color="white", linewidth=1)
ax.tick_params(which="minor", length=0)

for i in range(len(labels)):
    for j in range(len(labels)):
        ax.text(j, i, f"{corr.values[i, j]:.2f}", ha="center", va="center", fontsize=8)

fig.colorbar(im, ax=ax, shrink=0.7, label="Correlation")
ax.set_title("Correlation matrix: Motor Competence\nand Reading Performance")
plt.tight_layout()
plt.show()
```
