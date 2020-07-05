# -*- cod(ing: utf-8 -*-
"""

@author: 785055
"""
import random

def probability(variant):
    return find_score(variant) / high_score

def create_initial_population(number):
    """
    Generating the intial population from the number of queens
    """
    population = [[random.randint(1, number) for _ in range(number) ] for _ in range(10)]
    return population

def find_score(variant):
    """
    finding the score
    """
    horizontal_collisions = sum([variant.count(queen)-1 for queen in variant])/2
    diagonal_collisions = 0

    total_count = len(variant)
    left_diagonal = [0] * 2*total_count
    right_diagonal = [0] * 2*total_count
    for i in range(total_count):
        left_diagonal[i + variant[i] - 1] += 1
        right_diagonal[len(variant) - i + variant[i] - 2] += 1

    diagonal_collisions = 0
    for i in range(2*total_count-1):
        counter = 0
        if left_diagonal[i] > 1:
            counter += left_diagonal[i]-1
        if right_diagonal[i] > 1:
            counter += right_diagonal[i]-1
        diagonal_collisions += counter / (total_count-abs(i-total_count+1))
    return int(high_score - (horizontal_collisions + diagonal_collisions))

def random_select(population, probabilities):
    populationWithProbabilty = zip(population, probabilities)
    total = sum(w for c, w in populationWithProbabilty)
    r = random.uniform(0, total)
    upto = 0
    for c, w in zip(population, probabilities):
        if upto + w >= r:
            return c
        upto += w
    assert False, "Shouldn't get here"
    
def reproduce(x, y): #doing cross_over between two chromosomes
    n = len(x)
    c = random.randint(0, n - 1)
    return x[0:c] + y[c:n]

def mutate(x):  #randomly changing the value of a random index of a chromosome
    n = len(x)
    c = random.randint(0, n - 1)
    m = random.randint(1, n)
    x[c] = m
    return x

def print_chromosome(chrom):
    print("Chromosome = {},  Fitness = {}"
        .format(str(chrom), find_score(chrom)))

def genetic_queen(population, find_score):
    mutation_probability = 0.03
    new_population = []
    probabilities = [probability(each) for each in population]
    for i in range(len(population)):
        x = random_select(population, probabilities) 
        y = random_select(population, probabilities) 
        child = reproduce(x, y) 
        if random.random() < mutation_probability:
            child = mutate(child)
        # print_chromosome(child)
        new_population.append(child)
        if find_score(child) == high_score: break
    return new_population


if __name__ == "__main__":
    num = 8 #say N = 8
    global high_score
    high_score = (num*(num-1))/2
    print(high_score)
    initial_population = create_initial_population(num)
    generation = 1
    population_scores = [find_score(pop) for pop in initial_population]
    print(population_scores)
    while not high_score in population_scores:
        print("=== Generation {} ===".format(generation))
        population = genetic_queen(initial_population, find_score)
        print("")
        print("Maximum Fitness = {}".format(max([find_score(n) for n in population])))
        generation += 1
    output = []
    for each in population:
        if find_score(each) == high_score:
            print("One of the solutions: ")
            chrom_out = each
            print_chromosome(each)
    board = []
    for x in range(num):
        board.append(num-chrom_out[i])
    print(board)
        
    
    
        


