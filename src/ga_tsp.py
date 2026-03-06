import random
import numpy as np
from src.utils import calculate_route_distance, create_random_route

class GeneticAlgorithmTSP:

    def __init__(self, dist_matrix, population_size=60, mutation_rate=0.02, generations=200):
        self.dist_matrix = dist_matrix
        self.num_cities = len(dist_matrix)
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.generations = generations

    def initial_population(self):
        return [create_random_route(self.num_cities) for _ in range(self.population_size)]

    def fitness(self, route):
        return 1 / calculate_route_distance(route, self.dist_matrix)

    def selection(self, population, fitness_scores):
        idx = np.random.choice(len(population), p=fitness_scores)
        return population[idx]

    def crossover(self, parent1, parent2):
        start = random.randint(0, len(parent1)-2)
        end = random.randint(start+1, len(parent1)-1)

        child = parent1[start:end]
        child += [gene for gene in parent2 if gene not in child]
        return child

    def mutate(self, route):
        if random.random() < self.mutation_rate:
            i, j = random.sample(range(len(route)), 2)
            route[i], route[j] = route[j], route[i]
        return route

    def run(self):
        population = self.initial_population()

        best_route = None
        best_distance = float("inf")

        for gen in range(self.generations):
            fitness_scores = np.array([self.fitness(r) for r in population])
            fitness_scores /= fitness_scores.sum()

            new_population = []
            for _ in range(self.population_size):
                p1 = self.selection(population, fitness_scores)
                p2 = self.selection(population, fitness_scores)
                child = self.crossover(p1, p2)
                child = self.mutate(child)
                new_population.append(child)

            population = new_population

            # cek best di generasi ini
            for r in population:
                d = calculate_route_distance(r, self.dist_matrix)
                if d < best_distance:
                    best_route = r
                    best_distance = d

            print(f"Generasi {gen+1} | Best Distance: {best_distance:.4f}")

        return best_route, best_distance
