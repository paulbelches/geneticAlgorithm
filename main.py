import numpy as np
#inicialiar populación

population = None

def fitness1(v): 
    return 2 * v

def crossover1(v1, v2): 
    return (v1 + v2) // 2

def selection1(v): 
    return (v > 50)

def sort(population):
    return population[np.argsort(population[:, 1])[::-1]]

def fitness(population, function): 
    for i in range(len(population)):
        population[i][1] = function(population[i][0])
    return population

def crossover(population, function): 
    for i in range(len(population) - 1):
        newBorn = function(population[i][0], population[i+1][0])
        population = np.vstack((population, [newBorn,0]))
    return population

def mutation(population): 
    randomNumbers = np.random.random(len(population))
    for i in range(len(population)):
        if (randomNumbers[i] > 0.9):
            population[i][0] = population[i][0] + 1
    return population
    
def selection(population, function):
    selected = [] 
    for i in range(len(population)):
        if (function(population[i][0])):
            selected.append([population[i][0], population[i][1]])
    return np.array(selected)

def geneticAlgorithms(fitness, fitnessOperation, crossover, mutation, selection, population):
    fitness()
    #terminate
    selection()
    crossover()
    mutation()

population = np.random.randint(10, 100, (4, 2))
print(population)
#population = fitness(population, fitness1)
#print(population)
#population = selection(population, selection1)
#print(population)
#population = crossover(population, crossover1)
#print(population)
#population = mutation(population)
#print(population)
population = sort(population)
print(population)
