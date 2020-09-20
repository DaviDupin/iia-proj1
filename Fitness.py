#!/usr/bin/python
# coding=UTF-8
class Fitness:
    #Criando uma classe para calcular o Fitness de uma rota
    def __init__(self,route):
        self.route = route #cada fitness possui sua própria rota
        self.distance = 0 #a distancia será o parametro para medir o quão 'boa' é uma rota
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
                auxDistance += originCity.distance(destinyCity.id) #somando a distancia da rota completa
            self.distance = auxDistance
        return self.distance
    
    def fitCalc(self):
        if self.fit == 0:
            self.fit = 1/float(self.routeDistance()) #fórmula de fitness
        return self.fit
