# Problems: Feature Selection 
## Credit Risk Scoring

The benchmark presented in this folder applies a feature selection model to a
[credit risk scoring dataset](../../../datasets/credit_risk_data) where the data samples are $59$ dimensional.
A detailed description of the dataset can be found [here](../../../datasets/credit_risk_data/README.md).
For that purpose, we use a variational black-box binary optimization algorithm introduced in 
[Variational quantum algorithm for unconstrained black box binary
optimization: Application to feature selection](https://doi.org/10.22331/q-2023-01-26-909) and compare it to classical,
state-of-the-art heuristics, i.e., Recursive Feature Selection (RFE) and 
Recursive Feature Selection with Cross Validation (RFECV) -- both provided by [Scikit-learn(https://scikit-learn.org/stable/)]. 
It should be noted that the cross validation in RFECV can depend on various scoring functions. 
In our comparison, we use RFECV with accuracy respectively log-loss scoring.
The outcome of the variational quantum algorithm is accurately simulated with a 
matrix product state (MPS) simulator for a parameterized 
[RealAmplitudes](https://qiskit.org/documentation/stubs/qiskit.circuit.library.RealAmplitudes.html) ansatz with 
linear entanglement and depth $0, 1$ and $2$.

### Experiments and Results

- Variational quantum algorithm with depth $0$ Ansatz
   - [Summary of experimental setup](vqa_d0/summary.json)
   - [Performance Summary](vqa_d0/performance.csv)
   - [Training Summary](vqa_d0/training.csv)
- Variational quantum algorithm with depth $1$ Ansatz
   - [Summary of experimental setup](vqa_d1/summary.json)
   - [Performance Summary](vqa_d1/performance.csv)
   - [Training Summary](vqa_d1/training.csv)
- Variational quantum algorithm with depth $2$ Ansatz
   - [Summary of experimental setup](vqa_d2/summary.json)
   - [Performance Summary](vqa_d2/performance.csv)
   - [Training Summary](vqa_d2/training.csv)
- RFE
   - [Summary of experimental setup](rfe/summary.json)
   - [Performance Summary](rfe/performance.csv)
- RFECV (accuracy)
   - [Summary of experimental setup](rfecv_acc/summary.json)
   - [Performance Summary](rfecv_acc/performance.csv)
- RFECV (log-loss)
  - [Summary of experimental setup](rfecv_log/summary.json)
  - [Performance Summary](rfecv_log/performance.csv)