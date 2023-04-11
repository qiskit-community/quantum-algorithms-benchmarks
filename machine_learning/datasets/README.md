# Datasets

The goal of this directory is to make a set of relevant datasets accessible for machine learning benchmarks.
Hence, the files in this directory are supposed to either load data from publicly available 
online resources or to generate data themselves.

## Data Loading Files
A data loading file is supposed to reference the online resource where the data is available. 
An example for loading credit risk data is given in the [following file](credit_risk_data/load_credit_risk_data.py). 

## Data Generating Files
A data generating file is supposed to implement a well documented script that generates a dataset. 
Additionally, the data generating script should be executed and the resulting train/test data should be 
stored--preferably in a pickle format.

## List of Available Datasets

| Description      | Directory                            | Loaded/Generated | Number Data Samples | Data Dimension |
|------------------|--------------------------------------|------------------|---------------------|----------------|
| Credit Risk Data | [credit_risk_data](credit_risk_data) | Loaded           | 1000                | 59             |

