---
file_format: mystnb
kernelspec:
  name: python3
  display_name: Python 3
  language: python
---

% ARQUIVO GERADO por docs/conf.py. Não edite aqui: edite ../../src/amazonasdatahub/documentations/malaria_amazonas.md


```{include} ../../src/amazonasdatahub/documentations/malaria_amazonas.md
:relative-images:
:start-line: 3
:end-line: 190
```

### Example

```{code-cell} python
import matplotlib.pyplot as plt
from amazonasdatahub.datasets import get_dataset

# Load dataset
malaria_amazonas = get_dataset("malaria_amazonas")

# Filter by year 2019 and count exam results
counts = (
    malaria_amazonas[malaria_amazonas["exam_year"] == 2019]["exam_result"]
    .value_counts()
)

# Plot bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(counts.index, counts.values, color="skyblue", edgecolor="gray")

# Add text labels on top of bars
ax.bar_label(bars, padding=3)

# Titles and labels
ax.set_title(
    "Results of malaria tests conducted in 2019\nDocumented cases in Amazonas and of patients residing in the state",
    fontsize=10,
    loc="left"
)
ax.set_xlabel("Result")
ax.set_ylabel("Count")

plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
```
