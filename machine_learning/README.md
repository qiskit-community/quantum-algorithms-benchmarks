# Benchmarking quantum machine learning for finance

This subdirectory holds the machine learning track of the benchmarks of quantum computing algorithms.

## Problem definitions

To benchmark quantum algorithms for [machine learning problems](problems), we consider a variety of benchmarks.
The benchmarks include

* Classification such as fraud detection or customer analysis
* Forecasting
* Feature selection
* etc.

The benchmarks are based on the following quantum algorithms

* [Variational quantum classifier (VQC)](https://github.com/Qiskit/qiskit-machine-learning/blob/main/qiskit_machine_learning/algorithms/classifiers/vqc.py) 
* [Quantum support vector machine classifier (QSVC)](https://github.com/Qiskit/qiskit-machine-learning/blob/main/qiskit_machine_learning/algorithms/classifiers/qsvc.py)
* [Neural network classifier](https://github.com/Qiskit/qiskit-machine-learning/blob/main/qiskit_machine_learning/algorithms/classifiers/neural_network_classifier.py)
* [Black-box binary optimizations (BBBO)](https://quantum-journal.org/papers/q-2023-01-26-909/)
* etc.

## Metrics  

For each of the above mentioned algorithms this repository provides the tools to benchmark these problems with respect to the following metrics.

* **Performance** is measured with respect to standard ML metrics such as accuracy, recall and precision.

* **Resource requirements** is measured considering various aspects: the training time, the inference time of a model, and the amount of data required to train a model up to a pre-defined accuracy.
  For the temporal metrics, it should be noted that this includes the classical pre-processing time it takes to prepares the quantum circuits as well as the execution of the quantum circuits - except for queuing time.
  
* **Intrinsic model properties** This class of metrics includes generalization bounds and capacity measures.

## Datasets

To support comparability, we provide a [set of datasets](datasets) which are relevant for the benchmarking problems given above.
Notably, some of the references below provide links to publicly available online resources and other link to files which generate a benchmarking dataset.


## Benchmark and result summaries

Novel benchmarks and respective results are to be summarized in a standardized format including model, backend, training results, etc.
Templates to summarize the models in *.json* and training parameters as well as final results in *.csv* format can be found in [problems](problems).

The presentation of an existing publication as a benchmark may be done in the form of a notebook as shown [in the following example](problems/feature_selection/credit_risk1/results.ipynb). 

## Ways to contribute
* **Contribute a new dataset:** Benchmarking strongly relies on the availability of suitable data. One way to contribute to this benchmarking repository is to either provide a script that loads publicly available data in a reproducible way or a script that directly generates a dataset. 
* **Contribute a new benchmarking problem:** As soon as we have data, the next question is: What do we want to benchmark with it? Hence, another way to contribute is to propose a benchmarking problem with a suitable description.
* **Contribute a new solution:** Finally, if you want to challenge existing benchmarking solutions, you can also contribute your own solution with your algorithmic setting of choice to the repo and document it according to the provided templates.