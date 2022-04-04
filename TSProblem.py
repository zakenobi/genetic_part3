# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(GA solving TSP example)
"""
from GASolver_module import GAProblem
import cities_module
import random

class TSProblem(GAProblem):
    """Implementation of GAProblem for the traveling salesperson problem"""
    
    def __init__(self):
        """Initializes a TSProblem"""
        # Retrieve problem module
        self.generateIndividual = self.generateIndividual
        self.mutate = self.mutate
        self.evaluate = self.evaluate
        self.sortPopulation = self.sortPopulation

    def generateIndividual(self):
        """Generates an individual for the problem"""
        # Generate a random individual
        chromosome = cities_module.defaultRoad(cities)
        # Shuffle the chromosome
        random.shuffle(chromosome)
        # Calculate the individual's fitness
        fitness = cities_module.roadLength(cities, chromosome)
        # return the fitness and the chromosome
        return chromosome, fitness

    def sortPopulation(self, population: list):
        population.sort(reverse=True)
        return population

    def mutate(self, population: list, middle: int, mutation_rate: float):
        # Get two random good individuals
        chromosome_1 = population[random.randint(middle, len(population)-1)]
        chromosome_2 = population[random.randint(middle, len(population)-1)]

        # Make a list of 12 numbers between 0 and 11
        cities_copy = []
        for j in range(12):
            cities_copy.append(j)

        # Create empty chromosome
        new_chromosome = []

        # Loop 6 times
        for j in range(6):
            city = chromosome_1.chromosome[j]
            new_chromosome.append(city)
            # Remove the city from the copy of the cities
            cities_copy.remove(city)

        # Loop from 6 to 12
        for j in range(6, 12):
            city = chromosome_2.chromosome[j]
            # Check if the city is in the copy of the cities
            if city in cities_copy:
                # Add the city to the new chromosome
                new_chromosome.append(city)
                # Remove the city from the copy of the cities
                cities_copy.remove(city)
            else:
                city =cities_copy[random.randint(0, len(cities_copy)-1)]
                # Add a random city to the new chromosome from the copy of the cities
                new_chromosome.append(city)
                # Remove the city from the copy of the cities
                cities_copy.remove(city)

        # Return the new chromosome
        return new_chromosome

    def evaluate(self, chromosome: list):
        """Evaluates the fitness of an individual"""
        # Calculate the individual's fitness
        fitness = cities_module.roadLength(cities, chromosome)
        # Return the fitness
        return fitness

        



if __name__ == '__main__':

    from GASolver_module import GASolver

    cities = cities_module.loadCities("cities.txt")
    problem = TSProblem()
    solver = GASolver(problem)
    solver.resetPopulation()
    # print the population
    print(solver._population)
    solver.evolveForOneGeneration()
    solver.evolveUntil()
    cities_module.drawCities(cities, solver.getBestIndividual().chromosome)
