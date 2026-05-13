---
title: "rionegro_amazonas"
---

# rionegro_amazonas

A dataset of the Rio Negro River (Amazonas) level from 2003 to 2023.

### Description

This dataset contains data of the Rio Negro River level in the state of Amazonas (Brazil), compiling information on years, semesters and days, along with the river's level in meters and whether it filled or dropped (in centimeters).

### Usage

```python
rionegro_amazonas = get_dataset("rionegro_amazonas")
```

### Format

‘rionegro_amazonas’ A data frame with 8003 rows and 7 columns:

#### level_m

River level in meters

#### increase_decrease_cm

Wheter the river level filled or dropped (in centimeters)

#### day

Measurement day

#### month

Measurement month

#### year

Measurement year

#### semester

Measurement semester

### Source

https://portodemanaus.com.br/nivel-do-rio-negro/
