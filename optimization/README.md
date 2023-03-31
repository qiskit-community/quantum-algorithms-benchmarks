# Benchmarks for optimization problems

Welcome to the optimization benchmarks. 
In this repository you will find a set of classical optimization problems and a description 
of known solutions using quantum and/or classical hardware.
This repository is organized according to the following structure, where problems are organized following their type:

- optimization/
    - problems/
        - maxcut/
            - instance_1/
                - solution_1
                - ...

Every problem should contain a clear description, and every solution needs to contain the defined metrics as well as sufficient information to be reproducible.


### Benchmarking metrics

A proposed solution to a benchmark optimization problem must report its performance.
This repository allows solutions to report at least one of the following metrics.

* **Objective** captures how good the solution is. For example, a MaxCut problem minimized
  with QAOA may report the size of the best cut it finds.
  
* **Approximation ratio** the approximation ratio to the problem. This metric can be reported
  if the optimal solution to the problem is known.
  
* **Time to solution** includes the time it took to execute the quantum algorithm. Any contributed
  solution that reports the time to solution should make clear what this includes. For instance,
  a benchmark with a solution obtained with a variational algorithm should specify if the time
  to solution includes the training of the variational parameters, queueing to run, etc. 
  Some care must be taken in reporting the time to solution since a family of problems may be solved by training the 
  variational algorithm once and reusing the optimal parameters.
  
* **Computational Resources** reports the resources needed to obtain the solution. This may
  include, for instance, the type of hardware used expressed as the type and number
  of CPUs and QPUs used to obtain the solution.
  Benchmarks that report this metric must clearly define what it includes and how
  it is measured. Note that computational resources accepts multiple entries to describe
  complex hardware settings that, for instance, combine multiple computational units. 

A proposed solution to a benchmark should clearly define what metric it is reporting and how it
is defined. These benchmarks help evaluate the merit of different quantum approaches to 
optimization problems. Indeed, good yet sub-optimal solutions may be acceptable compared to 
optimal ones if they can be obtained quickly enough. In other cases, businesses may be driven 
by the cost of obtaining solutions (either optimal or sub-optimal but good enough) which is
why the *Computational Resources* metric can be reported.

### Contributing a new problem

Each new problem or problem class should have its own folder.
This folder must contain either a method to generate the problems of the problem class, or a 
description of the optimization problem as an LP file if only one specific instance is contributed.
In addition, you may include alternative representations of the problem such as the Pauli 
operators it corresponds to.
A short README.md should be included to explain the intent of the problem and why it makes a
good benchmark.
The benchmark problem may be generic in nature, e.g., solve a Maxcut problem of a given size
and characteristics, or specific to an application, e.g., in finance.
For example, optimize a portfolio with a certain investment universe size under specified
constraints.

### Contributing a new solution

Solutions to a benchmark problem may be contributed in the folder of the problem.
Each solution should be in a sub-folder named ``solution_x`` where ``x`` is an index.
The solution can include the following files:
* A notebook to provide information on the solution such as hardware used, links to a
  paper with more details, transpilation steps, algorithm details.
* A ``summary.json`` file according to the ``summary_template.json`` template file found here.
* A ``performance.csv`` file that tracks the performance of the optimization algorithm
  throughout the optimization. This cvs file should include the following columns:
  `iteration number`, `best found solution`, `time`. Here, `iteration number` is the index of
  the iteration of the solver. It can represent, e.g., the number of evaluations of the cost 
  function or its gradient during the optimization. The `best found solution` is the value of
  the best solution found up until the corresponding iteration. The `time` column represents
  the time it took to arrive to the given point.

The notebook should provide enough information to reproduce the solution to the problem.
It is ok to provide a minimal notebook linking to published and open access papers
that describe the solution to the optimization problem.
Furthermore, the ``summary.json`` should clearly define the performance metrics that it 
reports. 
This file will be algorithmically parsed to report solutions at a high level in
the [summary notebook](/optimization/solution_summary.ipynb).
The schemas in ``summary_template.json`` must therefore be strictly adhered to.
If you are presenting solutions to instances of a problem class make sure to include 
these instances as LP files too or provide a link to where they can be found.
