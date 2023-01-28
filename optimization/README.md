# Benchmarks for optimization problems

Welcome to the optimization benchmarks. 
In this repository you will find a set of classical optimization problems and a description 
of known solutions using quantum and/or classical hardware.
This repository is organized according to the following structure:

- Optimization
    - problems
        - maxcut
        - ...
    - README.md

The problems are thus organized following their type.

### Benchmarking metrics

A proposed solution to a benchmark optimization problem must report on its performance.
This repository allows solutions to report at least one of the following metrics.

* **Solution quality** captures how good the solution is. For example, a MaxCut problem maximized
  with QAOA may report the approximation ratio of the best measured bitstring. A benchmark that
  reports a solution quality should clearly define how the metric is computed.
  
* **Time to solution** includes the time it took to execute the quantum algorithm. Any contributed
  benchmark that reports the time to solution should make clear what this includes. For instance,
  a benchmark with a solution obtained with a variational algorithm should specify if the time
  to solution includes the training of the variational parameters or not. Some care must be taken
  in reporting the time to solution since a family of problems may be solved by training the 
  variational algorithm once and reusing the optimal parameters.
  
* **Cost of solution** reports the ressources needed to obtain the solution. This may
  include, for instance, the price paid, or the amount of energy consumed to obtain the solution.
  Benchmarks that report a cost of solution must clearly define what this cost includes and how
  it is measured.

A proposed solution to a benchmark should clearly define what metric it is repporting and how it
is defined. These benchmarks help evaluate the merit of different quantum approaches to 
optimization problems. Indeed, good yet sub-optimal solutions may be acceptable compared to 
optimal ones if they can be obtained quickly enough. In other cases, businesses may be driven 
by the cost of obtaining solutions (either optimal or sub-optimal but good enough) which is
why the *cost of solution* metric can be reported.

### Contributing a new problem

Each new problem or problem class should have its own folder.
This folder must contain either a method to generate the problems of the problem class, or a 
description of the optimization problem as an LP file if only one specific instance is contributed.
In addition, you may include alternative representations of the problem such as the Pauli 
operators it corresponds to.
A short README.md should be included to explain the intent of the problem and why it makes a
good benchmark.
The benchmark problem may be generic in nature, e.g., solve a Maxcut problem of a given size
and characteristics, or specific to a financial application.
For example, optimize a portfolio with a certain investment universe size under specified
constraints.

### Contributing a new solution

Solutions to a benchmark problem may be contributed as short Jupyter notebooks included in the
folder of the problem.
The notebook should provide enough information to reproduce the solution to the problem.
Furthermore, the notebook should define the performance metrics that it reports.
It is acceptable to provide a minimal notebook linking to published and open access papers
that describe the solution to the optimization problem.
If you are presenting a solutions to instances of a problem class make sure to include 
these instances as LP files too.