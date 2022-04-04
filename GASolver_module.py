# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(generic genetic algorithm module)
"""


class Individual:
    """Represents an Individual for a genetic algorithm"""

    def __init__(self, chromosome: list, fitness: float):
        """Initializes an Individual for a genetic algorithm 

        Args:
            chromosome (list[]): a list representing the individual's chromosome
            fitness (float): the individual's fitness (the higher, the better the fitness)
        """
        self.chromosome = chromosome
        self.fitness = fitness

    def __lt__(self, other):
        """Implementation of the less_than comparator operator"""
        return self.fitness < other.fitness

    def __repr__(self):
        """Representation of the object for print calls"""
        return f'Indiv({self.fitness:.1f},{self.chromosome})'


class GAProblem:
    """Defines a Genetic algorithm problem to be solved by GASolver"""
    # Retreive problem module

    def __init__(self, chromosome:list, fitness:float):
        """Initializes a GAProblem"""

        self.chromosome = chromosome
        self.fitness = fitness
        
    def generateIndividual(self):
        """Generates an individual for the problem"""
        pass

    def mutate(self, population: list, middle: int, mutation_rate: float):
        """Mutates an individual"""
        pass

    def evaluate(self, chromosome: list):
        """Evaluates an individual"""
        pass

    def sortPopulation(self, population: list):
        """Sorts a population by fitness"""
        pass
   


class GASolver:
    def __init__(self, problem: GAProblem, selection_rate=0.5, mutation_rate=0.1):
        """Initializes an instance of a GASolver for a given GAProblem

        Args:
            problem (GAProblem): GAProblem to be solved by this GASolver
            selection_rate (float, optional): Selection rate between 0 and 1.0. Defaults to 0.5.
            mutation_rate (float, optional): mutation_rate between 0 and 1.0. Defaults to 0.1.
        """
        self._problem = problem
        self._selection_rate = selection_rate
        self._mutation_rate = mutation_rate
        self._population = []

    def resetPopulation(self, pop_size=50):
        """ Initialize the population with pop_size random Individuals """
        for i in range(pop_size):
            chromosome, fitness = self._problem.generateIndividual()
            self._population.append(Individual(chromosome, fitness))

    def evolveForOneGeneration(self):
        """ Apply the process for one generation : 
            -	Sort the population (Descending order)
            -	Remove x% of population (less adapted)
            -   Recreate the same quantity by crossing the surviving ones 
            -	For each new Individual, mutate with probability mutation_rate 
                i.e., mutate it if a random value is below mutation_rate"""
        
        # Sort the population
        self._population = self._problem.sortPopulation(self._population)



        # Getting the point of selection rate
        middle = int(self._selection_rate * len(self._population))
        # Loop through the population until the middle point
        for i in range(middle):
            chromosome = self._problem.mutate(self._population, middle, self._mutation_rate)
            fitness = self._problem.evaluate(chromosome)
            # Replace the individual
            self._population[i] = Individual(chromosome, fitness)
        

    def showGenerationSummary(self):
        """ Print some debug information on the current state of the population """
        #Print the population and the fitness of each individual
        #Sort the population
        self._population.sort(reverse=True)

        print("Population : ")
        for i in range(len(self._population)):
            print(self._population[i])
            print("\n")

    def getBestIndividual(self):
        """ Return the best Individual of the population """
        # Sort the population
        self._population = self._problem.sortPopulation(self._population)

        # Return the last element of the population
        return self._population[-1]
    

    def evolveUntil(self, max_nb_of_generations=500, threshold_fitness=None):
        """ Launch the evolveForOneGeneration function until one of the two condition is achieved : 
            - Max nb of generation is achieved
            - The fitness of the best Individual is greater than or equal to
              threshold_fitness
        """
        # Loop until the max number of generations is reached
        for i in range(max_nb_of_generations):
            self.evolveForOneGeneration()
            if threshold_fitness is not None:
                if self.getBestIndividual().fitness >= threshold_fitness:
                    break
