# Benchmarking quantum machine learning for finance

This subdirectory holds the machine learning track of the benchmarks of quantum computing for financial services.

## Problem definitions

To benchmark quantum solvers for quantum machine learning problems in a financial setting we consider finance oriented benchmarks and generic benchmarks.
The financial benchmarks include

* Fraud Detection
* Trading
* Customer Analysis
* Feature selection

The benchmarks are based on the following quantum algorithms

* [Variational quantum classifier (VQC)](https://github.com/Qiskit/qiskit-machine-learning/blob/main/qiskit_machine_learning/algorithms/classifiers/vqc.py) 
* [Quantum support vector machine classifier (QSVC)](https://github.com/Qiskit/qiskit-machine-learning/blob/main/qiskit_machine_learning/algorithms/classifiers/qsvc.py)
* [Neural network classifier](https://github.com/Qiskit/qiskit-machine-learning/blob/main/qiskit_machine_learning/algorithms/classifiers/neural_network_classifier.py)
* Black-box binary optimizations (BBBO)

## Metrics  

For each of the above mentioned algorithms this repository provides the tools to benchmark these problems with respect to the following metrics.

* **Performance** is measured with respect to standard ML metrics such as recall, accuracy and precision.

* **Resource requirements** is measured considering various aspects: the training time, the inference time of a model, and the amount of data required to train a model up to a pre-defined accuracy. to obtain a solution.
  For the temporal metrics, it should be noted that this includes the classical pre-processing time it takes to prepares the quantum circuits as well as the execution of the quantum circuits - except for queuing time.
  
* **Intrinsic model properties** This class of metrics includes generalization bounds and capacity measures.

## Datasets

To support comparability, we provide a set of datasets which are relevant for the benchmarking problems given above.
Notably, some of the references below provide links to publicly available online resources and other link to files which generate a benchmarking dataset.

* [Publicly available credit risk dataset](online:http://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data)
* GARCH data
* etc.

## Result summary

This section summarizes some results of the benchmarks. 
The table below has the key numbers but more importantly points to the file that runs the benchmark.

| Algorithm | Problem           | Dataset                 | Metric | Result | File |  Backend |
|-----------|-------------------|-------------------------|--------|--------|------|----------|
| VQC       | Fraud detection   | German Credit Risk Data |        |        |      |----------|
| BBBO      | Feature Selection |                         |        |        |      |----------|

