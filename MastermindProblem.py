# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(GA solving Mastermind example)
"""
from numpy import size
from GASolver_module import GAProblem
import mastermind_module as mm
import random


class MastermindProblem(GAProblem):
    """Implementation of GAProblem for the mastermind problem"""
    def __init__(self, size: int):
            """Initializes a TSProblem"""
            # Retrieve problem module
            self.generateIndividual = self.generateIndividual
            self.mutate = self.mutate
            self.evaluate = self.evaluate
            self.sortPopulation = self.sortPopulation
            self.size = size

    def generateIndividual(self):
        """Generates an individual for the problem"""
        # Generate a random individual
        chromosome = mm.generateRandomSecret(size=self.size)
        # Calculate the individual's fitness
        fitness = match.rateGuess(chromosome)
        # return the fitness and the chromosome
        return chromosome, fitness

    def sortPopulation(self, population: list):
        population.sort()
        return population

    def mutate(self, population: list, middle: int, mutation_rate: float):
        # Making children from the surviving individuals
        fitness=0
        while fitness < mutation_rate:
            chromosome = []

            # Loop size times -1
            for j in range(self.size-1):
                chromosome.append(population[random.randint(middle, len(population)-1)].chromosome[random.randint(0, self.size-1)])
            
            chromosome.append(random.randint(0, 5))

            fitness = match.rateGuess(chromosome)

        return chromosome

    def evaluate(self, chromosome: list):
        """Evaluates the fitness of an individual"""
        # Calculate the individual's fitness
        fitness = match.rateGuess(chromosome)
        # return the fitness and the chromosome
        return fitness


if __name__ == '__main__':

    from GASolver_module import GASolver

    match = mm.MastermindMatch(secretSize=8)
    problem = MastermindProblem(size = 8)
    solver = GASolver(problem)

    solver.resetPopulation()
    solver.evolveUntil()

    print(
        f"Best guess {solver.getBestIndividual()}")
    print(
        f"Problem solved? {match.isCorrect(solver.getBestIndividual().chromosome)}")

    # Print the solution