# Benchmarking Amplitude Estimation Algorithms

Amplitude Estimation (AE) has been first introduced by Brassard et al. (refered to here as "[Canonical AE](https://arxiv.org/abs/quant-ph/0005055)").
AE is an algorithm that may allow to speed-up many applications, such as derivative pricing or risk analysis.
In recent years, many variants of AE without quantum phase estimation have been proposed.
In the following, we give an overview of these variants as well as some of their properties and links to relevant papers.


| Algorithm | Year | Benchmarked | Comments |
|-----------|------|-------------|----------|
| [Maximum Likelihood AE (MLAE)](https://link.springer.com/article/10.1007/s11128-019-2565-2) | 2020 | TBD |                                       |
| [Iterative AE (IAE)](https://www.nature.com/articles/s41534-021-00379-1)                    | 2021 | TBD |                                       |
| [Low Depth AE](https://quantum-journal.org/papers/q-2022-06-27-745/)                        | 2022 | TBD |                                       |
| [Modified Iterative AE](https://arxiv.org/abs/2208.14612)                                   | 2022 | TBD | Asymptotically optimal variant of IAE |
| [Random Depth AE](https://arxiv.org/abs/2301.00528)                                         | 2023 | TBD |                                       |

In the directory 'results' we provide benchmarking results for these algorithms for different scenarios.
For every algorithm, benchmarks are done according to the following setting:

For every
- exact value $a^* = 0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99$,
- estimated/target accuracy (depending on the algorithm) $\epsilon = 10^{-k}, k = 1, \ldots, 6$, and
- confidence level $1-\alpha = 0.95$,

the considered algorithms are repeated 100 times and the number of calls to the oracle $Q$ is counted for each repetition.
Further, the actually achieve accuracy as well as the half-width of the a posteriori confidence intervals (for confidence level $1-\alpha$) are reported.
The corresponding algorithmic parameters to achieve the results should be given in a JSON dictionary in the column `config`.
The raw results are reported in the format (cf. [results/results_template.csv](results/results_template.csv)):


| algorithm | config | a_target | alpha | a_estimate | exact_error | ci_width    | num_oracle_calls |
|-----------|--------|----------|-------|------------|-------------|-------------|------------------|
| IAE       | {...}  | 0.25     | 0.05  | 0.28       | 0.03        | 0.12        | 100              |

The colums are defined as follows:
- `algorithm`: The name or abbreviation of the considered algorithm.
- `config`: A dictionary summarizing the algorithm settings for reproducability.
- `a_target`: The true `a^*` value of the considered problem.
- `alpha`: $(1-\alpha)$ determines the confidence level of the a posterori confidence intervals.
- `a_estimate`: The estimated `a` value returned by the algorithm.
- `exact_error`: The exact error between `a_target` and `a_estimate`.
- `ci_width`: The half-width of the a posteriori confidence interval, i.e., the estimate error.
- `num_oracle_calls`: The used number of oracle calls to achieve the reported results.

An overview of all available results is illustrated in the [results summary](results_summary.ipynb).


## How to contribute benchmarks

If you benchmarked some of the above algorithms or would like to contribute benchmarks for a new algorithm you can follow the steps below:

Create a pull request containing:
1. an updated version of the present page (updating the table of algorithms above)
2. a new folder with a README file describing what is being benchmarked and where the code to reproduce the results can be found,
3. a results file following the given format with the benchmarking results, and
4. an updated version of the results summary notebook.

