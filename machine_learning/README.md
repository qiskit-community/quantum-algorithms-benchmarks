# Benchmarking quantum machine learning

This subdirectory holds the machine learning track of the benchmarks of quantum computing algorithms. <br>
Quantum machine learning generally refers to the exploration of synergies between quantum computing and machine learning. 
The workflow typically involves the processing of given training data with an interplay of a classical and a quantum computer.


## Problem definitions

Since this repository is intended to benchmark quantum machine learning algorithms on well defined problems we aim to 
(i) compare quantum methods against each other, and 
(ii) compare quantum methods against state-of-the-art classical methods.
This requires a variety of *well defined* [machine learning problems](problems) on which to run the algorithms.
So far, these problems include

* Classification such as fraud detection or customer analysis
* Forecasting
* Feature selection
* etc.

Next, both the quantum and classical approaches to solve the problems must also be carefully specified.
For instance, the following quantum methods may be used to solve the problems outlined in this repository.

* [Variational quantum classifier (VQC)](https://github.com/Qiskit/qiskit-machine-learning/blob/main/qiskit_machine_learning/algorithms/classifiers/vqc.py) 
* [Quantum support vector machine classifier (QSVC)](https://github.com/Qiskit/qiskit-machine-learning/blob/main/qiskit_machine_learning/algorithms/classifiers/qsvc.py)
* [Neural network classifier](https://github.com/Qiskit/qiskit-machine-learning/blob/main/qiskit_machine_learning/algorithms/classifiers/neural_network_classifier.py)
* [Black-box binary optimizations (BBBO)](https://quantum-journal.org/papers/q-2023-01-26-909/)
* etc.

## Metrics  

For each of the above mentioned algorithms this repository provides the tools to benchmark these problems with respect to the following metrics.

* **Performance** are measured with respect to standard ML metrics on training and test data such as accuracy, recall and precision, and defined for each problem as appropriate.

* **Resource requirements** are measured considering various aspects: the training time, the inference time of a model, and the amount of data required to train a model up to a pre-defined accuracy.
  Temporal metrics should include the classical pre-processing time it takes to prepares the quantum circuits as well as the execution time of the quantum circuits. Queuing time should not be included.
  
* **Intrinsic model properties** include generalization bounds and capacity measures.

## Datasets

To support comparability, we define a [set of datasets](datasets), which are relevant for the benchmarking problems given above.
Notably, some of the references below provide links to publicly available online resources and other link to files which generate a benchmarking dataset.


## Benchmark and result summaries

Novel benchmarks and respective results are to be summarized in a standardized format including model, backend, training results, etc.
Templates to summarize the models in *.json* and training parameters as well as final results in *.csv* format can be found in [problems](problems).

The presentation of an existing publication as a benchmark may be done in the form of a notebook as shown [in the following example](problems/feature_selection/credit_risk1/results.ipynb). 

## Ways to contribute
* **Contribute a new dataset:** Benchmarking strongly relies on the availability of suitable data. One way to contribute to this benchmarking repository is to either provide a script that loads publicly available data in a reproducible way or a script that directly generates a dataset. When contributing a new data set it should be made clear how this dataset fits into the benchmarking framework. 
* **Contribute a new benchmarking problem:** As soon as we have data, the next question is: What do we want to benchmark with it? Hence, another way to contribute is to propose a benchmarking problem with a suitable description.
* **Contribute a new solution:** Finally, if you want to challenge any of the existing benchmarking solutions you can contribute your own solution to this repository. The solution must be documented according to the provided templates.
