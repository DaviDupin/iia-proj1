#!/usr/bin/python
# coding=UTF-8
import matplotlib.pyplot as plt, array
from operator import itemgetter
import City as c
import GenericCode as g

#transforma as rotas em cidades pra ficar legível
nameList = {
    "0": "BsB",
    "1": "PoA",
    "2": "BH",
    "3": "Carac.",
    "4": "Sant.",
    "5": "Bog.",
    "6": "Lima",
    "7": "RJ",
    "8": "BA",
    "9": "SP",
}
#determina se uma rota é válida ou não
def is_valid(pops):
    valid = True
    for i in range(0, len(pops)):
        if(len(pops[i]) >= 11):
            valid = pops[i][0].id == 0 and pops[i][10].id == 0 
        else:
            valid = False
    return valid

#recebendo a melhor rota disponível
bestRoute = g.generateBestRoute(population=c.cities, popSize=100, eliteSize=10, mutationRate=0.01, generations=100)
for i in range(0, len(bestRoute)):
    if(i+1 < len(bestRoute)):
        print(nameList[ str(bestRoute[i].id) ], end = ' -> ')
    else:
        print(nameList[ str(bestRoute[i].id) ])