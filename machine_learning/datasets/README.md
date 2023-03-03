# Datasets

The goal of this directory is to make a set of relevant datasets accessible for machine learning benchmarks.
Hence, the files in this directory are supposed to either load data from publicly available 
online resources or to generate data themselves.

## Data Loading Files
A data loading file is supposed to reference the online resource where the data is available and store the
loaded train/test data--preferably in a pickle format. An example for loading credit risk data is given in 
the [following file](credit_risk_data/load_credit_risk_data.py). 

## Data Generating Files
A data generating file is supposed to implement a well documented script that generates a dataset. 
Additionally, the data generating script should be executed and the resulting train/test data should be 
stored--preferably in a pickle format.

## Suggestions
- Link and load relevant [Kaggle](https://www.kaggle.com/) datasets
- Generate a GARCH dataset
- Link and load the data from publications such as [Benchmark Dataset for Mid-Price Forecasting of Limit
Order Book Data with Machine Learning Methods](https://arxiv.org/pdf/1705.03233.pdf)