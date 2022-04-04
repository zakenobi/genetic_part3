# Guide for GASolving
*By Manon LEMAIRE and Zachary GAGNOU*  
  
Description:  
This package is designed for solving genetic algorithm such as mastermind or tsp problems. In this package is included 5 modules:  
- GASolver_module.py
- mastermind_module.py
- cities_module.py
- MasstermindProblem.py
- TSPProblem.py  
  
## Generic scope
The generic code for solving these problems is in the GASolver_module.py file. It is composed of the following classes:
- Individual: the individuals that compose a given population.
- GAProblem: it calls the non generic code for solving a problem.
- GASolver: it calls the generic code for solving a problem.

## Specific scope
There are two examples of problems that can be solved with the gentic algorithm method: MASTERMIND and TSP.   

For each problem, there is a specific class that inherits from the GAProblem class located in the problem files. With each problem, there is a module that contains elements for utility functions and the class to instantiate the problem. There is also problem file that contains the specific code for solving the problem. This is the file run for getting the solution.

## Functions
The functions that are used for each problem are:
- resetPopulation: it initiate the population.
- evolveForOneGeneration: it evolves the population for one generation using 3 functions (sortPopulation, mutate and evaluate)
- showGenerationSummary: it prints the generation.
- getBestIndividual: it returns the best individual of the population.
- evolveUntil: it evolves the population until a given condition is met.
