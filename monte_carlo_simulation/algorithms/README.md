# Benchmarking Amplitude Estimation Algorithms

Amplitude Estimation (AE) has been first introduced by Brassard et al. (referred to here as "[Canonical AE](https://arxiv.org/abs/quant-ph/0005055)").
AE is an algorithm that may allow to speed-up many applications, such as derivative pricing or risk analysis.
In recent years, many variants of AE without quantum phase estimation have been proposed.
In the following, we give an overview of these variants as well as some of their properties and links to relevant papers.


| Algorithm | Year | Benchmarked | Comments |
|-----------|------|-------------|----------|
| [Maximum Likelihood AE (MLAE)](https://link.springer.com/article/10.1007/s11128-019-2565-2) | 2020 | TBD |                                        |
| [Iterative AE (IQAE)](https://www.nature.com/articles/s41534-021-00379-1)                   | 2021 | Yes |                                        |
| [Low Depth AE](https://quantum-journal.org/papers/q-2022-06-27-745/)                        | 2022 | TBD |                                        |
| [ChebPE](https://arxiv.org/abs/2207.08628)                                                  | 2022 | Yes | Variant of ChebAE for probabilities    |
| [Modified Iterative AE](https://arxiv.org/abs/2208.14612)                                   | 2022 | TBD | Asymptotically optimal variant of IQAE |
| [Random Depth AE](https://arxiv.org/abs/2301.00528)                                         | 2023 | TBD |                                        |

In the directory [results](/monte_carlo_simulation/algorithms/results/) we provide benchmarking results for these algorithms for different scenarios.

The objective of amplitude estimation is as follows. For an unknown amplitude $a_\text{target} \in [0,1]$, there is a quantum subroutine that for any $k \in \{0,1,2,...\}$ samples from Bernoulli random variable with parameter $\sin^2( (2k+1) \theta_\text{target}  )$ where $\theta_\text{target} = \arcsin(a_\text{target})$. Running this subroutine requires $k$ oracle calls. The objective is to estimate the probability $p_\text{target} := a^2_\text{target}$ using as few oracle calls as possible.

For every algorithm, 1000 data points are to be collected for all combinations of the following parameters:
- target probability $p_\text{target} = 0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99$,
- the desired accuracy $\epsilon = 10^{-k},$ where $k = 1, ..., 6$, and
- confidence level $1-\alpha = 0.95$,

The desired accuracy should inform the half-width of the a posteriori confidence intervals (for confidence level $1-\alpha$), but algorithms are not penalized for overshooting the desired accuracy. Further, the actually achieved accuracy is reported. The corresponding algorithmic parameters to achieve the results should be given in a JSON dictionary in the column `config`.
The raw results are reported in the format (cf. [results/results_template.csv](results/results_template.csv)):


| algorithm | config | epsilon | p_target | alpha | p_estimate | exact_error | ci_width    | num_oracle_calls |
|-----------|--------|---------|----------|-------|------------|-------------|-------------|------------------|
| IAE       | {...}  | 0.001   | 0.25     | 0.05  | 0.28       | 0.03        | 0.12        | 100              |

The columns are defined as follows:
- `algorithm`: The name or abbreviation of the considered algorithm.
- `config`: A dictionary summarizing the algorithm settings for reproducability.
- `epsilon`: The desired accuracy of the estimate. The final confidence interval may be smaller. 
- `p_target`: The true $p_\text{target}$ value of the considered problem.
- `alpha`: $(1-\alpha)$ determines the confidence level of the a posterori confidence intervals.
- `p_estimate`: The estimate of $p_\text{target}$ returned by the algorithm.
- `exact_error`: The distance between `p_target` and `p_estimate`. In a successful run this should be less than `ci_width`.
- `ci_width`: The half-width of the a posteriori confidence interval, which should be less than the desired accuracy $\epsilon$.
- `num_oracle_calls`: The number of oracle calls used to achieve the reported results.

An overview of all available results is illustrated in the [results summary](results_summary.ipynb).


## How to contribute benchmarks

If you benchmarked some of the above algorithms or would like to contribute benchmarks for a new algorithm you can follow the steps below:

Create a pull request containing:
1. an updated version of the present page (updating the table of algorithms above)
2. a new folder with a README file describing what is being benchmarked and where the code to reproduce the results can be found,
3. a results file following the given format with the benchmarking results, and
4. an updated version of the results summary notebook.

