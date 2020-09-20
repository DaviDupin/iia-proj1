#!/usr/bin/python
# coding=UTF-8
import random, pandas as pd, operator, numpy as np
import Fitness as f
def naturalSelection(population, poolSize):
    selectionResults = []
    df = pd.DataFrame(np.array(population), columns=["Index","Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100*df.cum_sum/df.Fitness.sum()
    
    for i in range(0, poolSize):
        selectionResults.append(population[i][0])
    for i in range(0, len(population) - poolSize):
        pick = 100*random.random()
        for i in range(0, len(population)):
            if pick <= df.iat[i,3]:
                selectionResults.append(population[i][0])
                break
    return selectionResults

def pool(population, selectionResults):
    matingpool = []
    for i in range(0, len(selectionResults)):
        index = selectionResults[i]
        matingpool.append(population[index])
    return matingpool


def reproduzir(parente1, parente2):
    child = []
    childP1 = []
    childP2 = []
    
    geneA = int(random.random() * len(parente1))
    geneB = int(random.random() * len(parente1))
    
    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        childP1.append(parente1[i])
        
    childP2 = [item for item in parente2 if item not in childP1]

    child = childP1 + childP2
    if(child[0].id != 0):
        for i in range(0, len(child)):
            if child[i].id == 0:
                c1 = child[0]
                c2 = child[i]
                child[0] = c2
                child[i] = c1
    if(len(child) >= 11):
        if(child[10].id != 0):
            for i in range(0, len(child)):
                if child[i].id == 0:
                    c1 = child[10]
                    c2 = child[i]
                    child[10] = c2
                    child[i] = c1
    else:
        child.insert(10, child[0])
    return child


def breedPopulation(matingpool, eliteSize):
    children = []
    length = len(matingpool) - eliteSize
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0,eliteSize):
        children.append(matingpool[i])
    
    for i in range(0, length):
        child = reproduzir(pool[i], pool[len(matingpool)-i-1])
        children.append(child)
    return children


def mutate(individual, mutationRate):
    for swapped in range(len(individual)):
        if(random.random() < mutationRate):
            swapWith = int(random.random() * len(individual))
            if (swapped != 0 and swapped != 10 and swapWith != 0 and swapWith != 10):
                city1 = individual[swapped]
                city2 = individual[swapWith]
                
                individual[swapped] = city2
                individual[swapWith] = city1
    return individual

def mutatePopulation(population, mutationRate):
    mutatedPop = []
    # print("populations..........:")
    # print(population[0][0].id)
    for ind in range(0, len(population)):
        mutatedInd = mutate(population[ind], mutationRate)
        mutatedPop.append(mutatedInd)
    return mutatedPop

#retorna uma sample (amostra) de cidades, formando uma rota
def randomRoute(city):
    route = random.sample(city, len(city))
    return route

#determina o fitness de uma população
def rankRoutes(population):
    fitnessResults = {}
    for i in range(0,len(population)):
        fitnessResults[i] = f.Fitness(population[i]).fitCalc() #para cada rota dentro da nossa população, calculamos o fitness
    return sorted(fitnessResults.items(), key = operator.itemgetter(1), reverse = True) #retorna uma array com o ID da rota e o valor de Fitness da mesma, por ondem descrescente

#seleciona

#pega (size) grupos aleatórios de rotas de viagem para criar uma geração inicial de rotas
def firstGen(size, city_array):
    pop = []
    bsb = city_array.pop(0) #primeiro removemos a primeira cidade, pois ela não deve estar em outro local ao não ser no inicio e fim
    for i in range(size):
        randRoute = randomRoute(city_array) #agora pegamos uma sample (amostra) de cidades, criando uma rota
        randRoute.insert(0, bsb) #após pegarmos a sample, vamo adicionar 'BsB' ao inicio da rota
        randRoute.insert(10, bsb) #e também ao fim da rota
        pop.append(randRoute) #por fim, adicionamos essa rota na nossa população
    return pop

def proxGene(currentGen, eliteSize, mutationRate):
    popRanked = rankRoutes(currentGen)

    selection = naturalSelection(popRanked, eliteSize)

    matingpool = pool(currentGen, selection)
    
    children = breedPopulation(matingpool, eliteSize)

    nextGeneration = mutatePopulation(children, mutationRate)

    return nextGeneration

#retorna a melhor rota possível
def generateBestRoute(population, popSize, eliteSize, mutationRate, generations):
    pop = firstGen(popSize, population)
    print("Distância Inicial: " + str(1 / rankRoutes(pop)[0][1]))
    for i in range(0, generations):
        pop = proxGene(pop, eliteSize, mutationRate)
    ranked = rankRoutes(pop)
    print("Final distance: " + str(1 / ranked[0][1]))
    bestRouteIndex = ranked[0][0]
    bestRoute = pop[bestRouteIndex]
    return bestRoute
