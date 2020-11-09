import numpy as np
#inicialiar populación

population = None
#Task 1
def f1(x1,x2):
  return (15*x1+30*x2+4*x1*x2-2*x1*x1-4*x2*x2)
def ver1(x1,x2):
  return (x1>=0 and x2>=0 and x1+2*x2<=30)

#Task 2
def f2(x1,x2):
  return (3*x1+5*x2)
def ver2(x1,x2):
  return (x1>=0 and x2>=0 and x1<=4 and 2*x2<=12 and 3*x1+2*x2<=18)

#Task 3
def f3(x1,x2):
  return (5*x1-x1*x1+8*x2-2*x2*x2)
def ver3(x1,x2):
  return (x1>=0 and x2>=0 and x1<=4 and 3*x1+2*x2<=6)


def fitness1(v1, v2): 
    return (15 * v1) + (30 * v2) + (4 * v1 * v2) - (2 * (v1**2)) - (4 * (v2**2)) 

def crossover1(v1, v2): 
    return [(v1[0] + v2[0]) / 2, (v1[1] + v2[1]) / 2, 0]

def selection1(v1, v2): 
    result = ((v1 + (2*v2)) <= 30) and (v1 >= 0) and (v2 >= 0)
    #print(result, v1, v2)
    return result

def sort(population):
    return population[np.argsort(population[:, 2])[::-1]]

def fitness(population, function): 
    for i in range(len(population)):
        population[i][2] = function(population[i][0], population[i][1])
    return population

def crossover(population, function): 
    for i in range(len(population) - 1):
        newBorn = function(population[i], population[i+1])
        population = np.vstack((population, [newBorn]))
    return population

def mutation(population): 
    randomNumbers = np.random.random(len(population))
    for i in range(len(population)):
        if (randomNumbers[i] > 0.9): 
            population[i][0] = population[i][0] + 1
            population[i][1] = population[i][1] + 1
        if (randomNumbers[i] < 0.1):
            population[i][0] = population[i][0] - 1
            population[i][1] = population[i][1] - 1
    return population
    
def selection(population, function):
    selected = [] 
    for i in range(len(population)):
        if (function(population[i][0], population[i][1])):
            selected.append(population[i])
    return np.array(selected[:101])

def geneticAlgorithms(fitness, fintnessFunction, crossover, crossoverFunction, mutation, selection, selectionFunction, 
    sort,  population, generations):
    cont = 0
    while (True):
        cont += 1
        population = selection(population, selectionFunction)
        population = fitness(population, fintnessFunction)
        population = sort(population)
        if (cont ==  generations):
            return population
        population = crossover(population, crossoverFunction)
        population = mutation(population)

population = np.random.randint(1, 100, (1000000, 3))
population1 = geneticAlgorithms(fitness, fitness1, crossover, crossover1, mutation, selection, selection1, sort,  population, 100)
print(population1[0])
population2 = geneticAlgorithms(fitness, f2, crossover, crossover1, mutation, selection, ver2, sort,  population, 100)
print(population2[0])
population3 = geneticAlgorithms(fitness, f3, crossover, crossover1, mutation, selection, ver3, sort,  population, 100)
print(population3[0])