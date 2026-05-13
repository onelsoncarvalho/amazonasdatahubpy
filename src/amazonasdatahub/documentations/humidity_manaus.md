---
title: "humidity_manaus"
---

# humidity_manaus

Time series with Extreme Values of Limited Range

### Description

A time series dataset consisting of the minimum relative humidity observed in the city of Manaus from January 2009 to December 2020. This dataset is a sample of size n = 144 monthly blocks.


### Usage

```python
humidity_manaus = get_dataset("humidity_manaus")
```

### Format

‘humidity_manaus’ A tibble with 144 rows and 5 columns

#### year

The year in which this data was observed

#### rh

Relative Humidity

#### dbt

Dry Bulb Temperature

#### wbt

Wet Bulb Temperature

#### month

The month in which this data was observed


### Source

NASCIMENTO, Leonardo Brandão Freitas; LIMA, Max Sousa; DUCZMAL, Luiz H. P-min-stable regression models for time series with extreme values of limited range. Environmetrics, Issue 2, v. 36, 2025.
