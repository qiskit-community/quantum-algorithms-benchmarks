# Datasets: Credit Risk

This folder enables the loading of a publicly 
available [credit risk data set](http://archive.ics.uci.edu/ml/machine-learning-databases/statlog/)
$X$ with corresponding labels $y$ which is made available by the UCI machine learning repository. 
The data set includes $1000$ data points which determine the credit-worthiness of a customer with respect to $20$ attributes. 
Notably, the categorical features of the original data set are one-hot encoded. 
Thus, the dimension of the final feature vector grows to $59$.
This fact allows us to directly conclude that the individual features are not linearly independent.

Files:
- [Data Loading File](load_credit_risk_data.py)
- [Train Data Indices for Pre-Loaded Data Split](train_indices.npy)
- [Test Data Indices for Pre-Loaded Data Split](test_indices.npy)
