# Misinformation and the Factors Leading to Spread and Belief

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>


## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         Misinformation Analysis and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── Misinformation Analysis   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes Misinformation Analysis a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```
## Description
This project was created to help analyze what factors are more likely to lead to the spread and greater belief in sources of misinformation.

## Dependicies
```
.pandas
.seaborn
.matplotlib
.pointbiserialr from scipy.stats
.mannwhitneyu from scipy.stats
```
## Setting up the enviornment
When it comes to setting the enviorment, you will first want to get the data. The link to the data is right below.
```
https://www.kaggle.com/code/venomsnake/aren-t-birds-real-examining-a-modern-conspiracy/input
```
After downloading the dataset you will want to read this dataset into your porgram. The code to do this is below.
```
import pandas as pd
df= pd.read_csv("birds_arent_real_tweets.csv")
df.head()
```


--------

