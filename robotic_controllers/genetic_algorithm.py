import random


class GeneticAlgorithm(object):

    def __init__(self, population_size, mutation_rate, crossover_rate, elitism_count, tournament_size):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.elitism_count = elitism_count
        self.tournament_size = tournament_size

    def init_population(self, chromosome_length):
        p = Population(self.population_size, chromosome_length)
        return p

    def mutate_population(self, population):
        new_population = Population(len(population))
        for population_idx in range(len(population)):
            individual = population.getfittest(population_idx)
            for gene_idx in range(len(individual.chromosome)):
                if population_idx >= self.elitism_count:
                    if self.mutation_rate > random.random():
                        new_gene = 1
                        if individual.chromosome[gene_idx] == 1:
                            new_gene = 0
                        individual.chromosome[gene_idx] = new_gene
            new_population.population[population_idx] = individual
        return new_population


class Individual(object):

    def __init__(self, chromosome, fitness=-1):
        if isinstance(chromosome, int):
            self.chromosome = [0] * chromosome
            for i in range(chromosome):
                if 0.5 < random.random():
                    self.chromosome[i] = 1
        else:
            self.chromosome = chromosome
        self.fitness = fitness

    def __str__(self):
        return ', '.join(str(c) for c in self.chromosome)


class Population(object):

    def __init__(self, population_size, chromosome_length=None, fitness=0):
        self.population = [None] * population_size
        self.fitness = fitness
        if chromosome_length is not None:
            for i in range(len(self.population)):
                self.population[i] = Individual(chromosome_length)

    def getfittest(self, offset):
        s = sorted(self.population, key=lambda individual: individual.fitness, reverse=True)
        return s[offset]

    def __len__(self):
        return len(self.population)

    def set_individual(self, offset, individual):
        self.population[offset] = individual

    def get_individual(self, offset):
        return self.population[offset]

    def shuffle(self):
        random.shuffle(self.population)




