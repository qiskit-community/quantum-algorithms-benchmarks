# Benchmarking Amlitude Estimation Algorithms

Amplitude Estimation (AE) has been first introduced by Brassard et al. (refered to here as "[Canonical AE](https://arxiv.org/abs/quant-ph/0005055)").
In recent years, many variants without the requirement of quantum phase estimation have been proposed.
In the following, we give an overview of these variants as well as some of their properties and links to relevant papers.


| Algorithm | Year | Benchmarked | Comments | Code To Generate Results |
|-----------|------|-------------|----------|------|
| [Maximum Likelihood AE (MLAE)](https://link.springer.com/article/10.1007/s11128-019-2565-2) | 2020 | No |                                       | https://github.com/Qiskit/qiskit-terra/blob/main/qiskit/algorithms/amplitude_estimators/mlae.py
| [Iterative AE (IAE)](https://www.nature.com/articles/s41534-021-00379-1)                    | 2021 | No |                                       | https://github.com/Qiskit/qiskit-terra/blob/main/qiskit/algorithms/amplitude_estimators/iae.py |
| [Low Depth AE](https://quantum-journal.org/papers/q-2022-06-27-745/)                        | 2022 | No |                                       | |
| [Modified Iterative AE](https://arxiv.org/abs/2208.14612)                                   | 2022 | No | Asymptotically optimal variant of IAE | |
| [Random Depth AE](https://arxiv.org/abs/2301.00528)                                         | 2023 | No |                                       | |

In the directory 'benchmarks' we provide benchmarking results for these algorithms for different target accuracies as well as problem settings.

Benchmarks are done according to the following setting:

For every 
- exact target value $a^* = 0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99$,
- target accuracy $\epsilon = 10^{-k}, k = 1, \ldots, 6$, and
- confidence level $\alpha = 0.9, 0.95, 0.99$,

the analyzed algorithms are repeated 100 times and the number of calls to the oracle $Q$ is counted and reported in terms of the mean and standard deviation over the 100 repetitions. The corresponding algorithmic parameters should be given in a JSON dictionary in the column `params`.
The raw results are then reported in the format (cf. `results/results_template.csv`).


| algorithm | a_target | epsilon_target | alpha | mean_oracle_calls | stdev_oracle_calls | params | repetitions |
|-----------|----------|----------------|-------|-------------------|--------------------|--------|-------------|
| IAE       | 0.25     | 1e-3           | 0.05  | ...               | ...                | ...    | 100         |

The available results are illustrated in `results.ipynb`.

The benchmarked algorithms can be provided in terms of code (see `code/ae_variant_template.py` and/or results).

## How to contribute benchmarks

If you benchmarked some of the above algorithms or would like to contribute a new algorithm you can follow the steps below:

Create a pull request containing:
1. an updated version of the present page (updating the table of algorithms above)
2. a results file following the given format with the benchmarking results
3. an updating version of the results notebook
