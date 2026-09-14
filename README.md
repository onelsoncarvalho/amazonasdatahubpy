# amazonasdatahub

![amazonasdatahub logo](assets/figures/logo_amazonasdatahub_small.png)
<!-- badges: start -->

<!-- badges: end -->

The goal of `amazonasdatahub` is to aggregate databases from the State
of Amazonas (AM), Brazil, for conducting studies and preparing
educational materials, as well as to facilitate access to organized and
processed data, thereby supporting research and teaching and enabling
the application of statistical methods.

Full documentation of both Python and R versions is available in the
following languages/Documentação das versões em Python e R estão
disponíveis nos seguintes idiomas:

- [English
  documentation](https://onelsoncarvalho.github.io/amazonasdatahubsite/en)
- [🇧🇷 Documentação em Português
  (BR)](https://onelsoncarvalho.github.io/amazonasdatahubsite)

Python only documentation:

- [English documentation for Python
  version](https://onelsoncarvalho.github.io/amazonasdatahub)
- [🇧🇷 Documentação em Português (BR) para versão do
  Python](https://onelsoncarvalho.github.io/amazonasdatahub/br)

## Overview

This `amazonasdatahub` package provides databases from various types and
sources, all of which concern the State of Amazonas.

List of available datasets:

| Dataset | Area | Source |
|:---|:--:|:---|
| agriculture_amazonas | Agriculture and Livestock | Institute of Agricultural and Sustainable Forestry Development of the State of Amazonas - 2024 |
| aids_amazonas | Health | Department of HIV, AIDS, Tuberculosis, Viral Hepatitis, and Sexually Transmitted Infections, 2024 |
| gdp_amazonas | Economy | Scientific Journal of Applied Social and Clinical Science - TIME SERIES ANALYSIS FOR THE QUARTERLY GROSS DOMESTIC PRODUCT OF AMAZONAS |
| humidity_manaus | Climate | NASCIMENTO, Leonardo Brandão Freitas; LIMA, Max Sousa; DUCZMAL, Luiz H. P-min-stable regression models for time series with extreme values of limited range. Environmetrics, Issue 2, v. 36, 2025. |
| malaria_amazonas | Health | Lais Baroni, M. P. (2020). An Integrated Dataset of Malaria Notifications in the Legal Amazon (Dataset). Synapse. <https://doi.org/10.7303/SYN21552203> |
| prf_amazonas | Road Safety | Brasil. Polícia Rodoviária Federal (PRF). Dados Abertos da PRF: Acidentes de Trânsito |
| rionegro_amazonas | Environment | Porto de Manaus. Nível do Rio Negro |
| srl_muni | Education | ALMEIDA, Thiago da Cruz de. Physical Literacy e desempenho em leitura de escolares amazônicos: um estudo de associação. 2024. 104 f. Dissertação (Mestrado em Educação) - Universidade Federal do Amazonas, Manaus, 2024. |

## Installation

To install `amazonasdatahub`, you need the following tools installed on your computer or development environment:

- Python 3.14.3
- `pip` (package manager)
- Git

You can install the development version of `amazonasdatahub` using `git clone` to clone the remote repository into your local environment and `pip` to install it:
``` 
# cloning
git clone https://github.com/onelsoncarvalho/amazonasdatahubpy amazonasdatahub
cd amazonasdatahub

# installing
pip install amazonasdatahub
```

## Usage and Examples

### Loading `amazonasdatahub`

Use `import` and `from` to require the functions from `datasets` module of `amazonasdatahub`:

``` python
from amazonasdatahub.datasets import get_dataset
```

The dataset name should be provided as argument of `get_dataset(dataset: str)` function.

```python
agriculture_amazonas = get_dataset('agriculture_amazonas')
aids_amazonas = get_dataset('aids_amazonas')
gdp_amazonas = get_dataset('gdp_amazonas')
```

### Get dataset documentation

Each dataset has its own documentation to provide the user information about the dataset variables.

Use `import` and `from` to require the functions from `docs` module:

```python
from amazonasdatahub.docs import get_doc
```

The dataset name should be provided as argument of `get_docs(dataset: str)` function.

```python
get_doc('agriculture_amazonas')
get_doc('aids_amazonas')
get_doc('gdp_amazonas')
```

<!-- ### Examples

#### Disease occurrence

The dataset `aids_amazonas` contains data of the AIDS occurrences in
each municipality from Amazonas.

One of the analysis that can be made is: visualize the time series of
counts filtered by municipality, where each case is grouped by the
sex/gender of each observation. To do this, we will use the dplyr
package to structure the data and the ggplot2 package to create and
customize the chart.

``` r
# Loading dplyr and ggplot to structure the data
require(dplyr)
require(ggplot2)
```

``` r
# Filtering by municipality and plotting case count by gender
aids_amazonas %>%
  filter(name_muni == "Manaus") %>%
  group_by(gender) %>%
  ggplot(aes(x = year, y = cases, group = gender, color = gender)) +
  geom_line() +
  scale_color_manual(values = c("blue", "red")) +
  theme_minimal() +
  labs(
    title = "AIDS occurrences in Manaus (2011-2023)",
    x = "Year",
    y = "Case count",
    color = "Gender"
  )
```

<img src="man/figures/README-unnamed-chunk-6-1.png" alt="" width="100%" />

#### Time Series

The `humidity_manaus` consists of the minimum relative humidity observed
in the city of Manaus from January 2009 to December 2020. We can
visualize the time series of the relative humidity during this time
interval.

Using `dplyr`, it is possible to create a date column, which will be
composed of the month and year. Using`ggplot2`, the time series chart
can be plotted.

``` r
# Loading dplyr and ggplot to structure the data
require(dplyr)
require(ggplot2)

# Creating date column and plotting the time series
humidity_manaus %>%
  mutate(date = as.Date(paste0(year, "-", month, "-","01"))) %>%
  ggplot(aes(x = date, y = rh)) +
  geom_line() +
  theme_minimal() +
  labs(
    title = "Relative Humidity of Amazonas (2009-2020)",
    x = "Date",
    y = "Relative Humidity"
  )
```

<img src="man/figures/README-unnamed-chunk-7-1.png" alt="" width="100%" /> -->


## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`amazonasdatahub` was created by Nelson Geraldo Aquino de Carvalho. It is licensed under the terms of the MIT license.

<!-- ## Credits

`amazonasdatahub` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter). -->

## Citation

- CARVALHO, Nelson Geraldo Aquino de; NASCIMENTO, Leonardo Brandão
  Freitas do. **amazonasdatahub**. 2026.
  <https://onelsoncarvalho.github.io/amazonasdatahubpy>.

