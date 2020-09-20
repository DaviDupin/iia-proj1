# The standard way to import NumPy:
import numpy as np, random, operator, pandas as pd, matplotlib.pyplot as plt
from operator import itemgetter

#transforma as rotas em cidades pra ficar legível
def nameConvert(cityRoutes):
    namesList = []
    for i in range (0,len(cityRoutes)):
        if cityRoutes[i] == [0,9,23,9,32,37,30,35,6,16]:
            namesList.append("BsB")
        elif cityRoutes[i] == [9,0,17,3,35,43,26,44,5,8]:
            namesList.append("SP")
        elif cityRoutes[i] == [23,17,0,20,31,47,11,51,22,8]:
            namesList.append("BA")
        elif cityRoutes[i] == [9,3,20,0,38,45,29,45,3,11,9]:
            namesList.append("RJ")
        elif cityRoutes[i] == [32,35,31,38,0,19,25,27,36,33]:
            namesList.append("Lima")
        elif cityRoutes[i] == [37,43,47,45,19,0,43,10,43,46]:
            namesList.append("Bog.")
        elif cityRoutes[i] == [30,26,11,29,25,43,0,49,30,19]:
            namesList.append("Sant.")
        elif cityRoutes[i] == [35,44,51,45,27,10,49,0,42,48]:
            namesList.append("Carac.")
        elif cityRoutes[i] == [6,5,22,3,36,43,30,42,0,13]:
            namesList.append("BH")
        elif cityRoutes[i] == [16,8,8,11,33,46,19,48,13,0]:
            namesList.append("PoA")
    return namesList

    return self.name.extend(["BsB", "SP", "BA", "RJ", "Lima", "Bog.", "Sant.", "Carac.", "BH", "PoA"])

class City:

    def list_distances(self): #tenho certeza que existe um método mais eficaz para isso, mas não encontrei. São os valores de distância entre as cidades (dados pelo projeto)
        self.list_distances = []
        self.list_distances.append([0,9,23,9,32,37,30,35,6,16]) #bsb
        self.list_distances.append([9,0,17,3,35,43,26,44,5,8]) #sp
        self.list_distances.append([23,17,0,20,31,47,11,51,22,8]) #ba
        self.list_distances.append([9,3,20,0,38,45,29,45,3,11,9]) #rj
        self.list_distances.append([32,35,31,38,0,19,25,27,36,33]) #lima
        self.list_distances.append([37,43,47,45,19,0,43,10,43,46]) #bog
        self.list_distances.append([30,26,11,29,25,43,0,49,30,19]) #sant
        self.list_distances.append([35,44,51,45,27,10,49,0,42,48]) #carac
        self.list_distances.append([6,5,22,3,36,43,30,42,0,13]) #bh
        self.list_distances.append([16,8,8,11,33,46,19,48,13,0]) #poa
        return self.list_distances

class Fitness:
    def __init__(self,route):
        self.route = route
        self.distance = 0
        self.fit = 0.0
    
    def routeDistance(self): #adaptado de towardsdatascience.com
        if self.distance == 0:
            auxDistance = 0
            for i in range (0, len(self.route)):
                originCity = self.route[i]
                destinyCity = None
                if i+1 < len(self.route):
                    destinyCity = self.route[i+1]
                else:
                    destinyCity = self.route[0]
                auxDistance += originCity.distance(destinyCity) #entender melhor essa parte
            self.distance = auxDistance
        return self.distance
    
    def fitCalc(self):
        if self.fit == 0:
            self.fit = 1/float(self.routeDistance()) 
        return self.fit

def randomRoute(city):
    route = random.sample(city, len(city))
    return route


#pega (size) grupos aleatórios de rotas de viagem
def firstGen(size, city):
    pop = []

    for i in range(size):
        pop.append(randomRoute(city))
    return pop

#determina o fitness
def rankRoutes(population):
    fitnessResults = {}
    for i in range(0,len(population)):
        fitnessResults[i] = Fitness(population[i]).fitCalc()
    print(sorted(fitnessResults, key = itemgetter(1), reverse = True))

def tspGA(population,size):
    pop = firstGen(size,population)
    
    for i in range(0, len(pop)):
        print(nameConvert(pop[i]),"\n")
    
    # primeiro cálculo de fitness tá com problema
    # print("Initial distance: " + str(1 / rankRoutes(pop)[0][1]))



cities = City()
distance = cities.list_distances()

tspGA(population=distance, size=10)

