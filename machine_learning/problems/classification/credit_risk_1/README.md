# Problems: Classification 
## Credit Risk Scoring

The benchmark presented in this folder applies a classification model to a 
[credit risk scoring dataset](../../../datasets/credit_risk_data).
A detailed description of the dataset can be found [here](../../../datasets/credit_risk_data/README.md).
For that purpose, we use a variational quantum classifier introduced in 
[Supervised learning with quantum-enhanced feature spaces](https://doi.org/10.1038/s41586-019-0980-2) with a
[ZZFeatureMap](https://qiskit.org/documentation/stubs/qiskit.circuit.library.ZZFeatureMap.html) 
for data loading and a parameterized 
[RealAmplitudes](https://qiskit.org/documentation/stubs/qiskit.circuit.library.RealAmplitudes.html) ansatz. 
Further information about the chosen model and training setting can be found [here](summary.json).

The model performance w.r.t. training and test data is summarized [here](performance.csv) and the evolution of 
the model parameters and the loss function value is presented [here](training.csv).