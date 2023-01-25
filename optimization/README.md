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

### Contributing a new problem

Each new problem or problem class should have its own folder.
This folder must contain either a method to generate the problems of the problem class, or a 
description of the optimization problem as a LP file if only one specific instance is contributed.
In addition, you may include alternative representations of the problem such as the Pauli 
operators it corresponds to.
Furthermore, the folder should contain a Jupyter Notebook that describes known solutions of 
the benchmark problem.
The notebook should provide enough information to reproduce the solution to the problem.
If you are presenting a solutions to instances of a problem class make sure to include these instances
as LP files too.