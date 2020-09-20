#!/usr/bin/python
# coding=UTF-8
class City:
    # criando lista de distancias; list_distances(id) = self.distance to city id
    def __init__(self, city_id, distances_array):
        self.id = city_id
        self.distances = distances_array

    def distance(self, city_id): #Retorna a distancia entre self.city e city_id
        return self.distances[city_id]


cities = [
    City(0, [0, 16, 6, 35, 30, 37, 32, 9, 23, 9]), #bsb

    City(1, [16, 0, 13, 48, 19, 46, 33, 11, 8, 8]), #poa

    City(2, [6, 13, 0, 42, 30, 43, 36, 3, 22, 5]), #bh

    City(3, [35, 48, 42, 0, 49, 10, 27, 45, 51, 44]), #carac

    City(4, [30, 19, 30, 49, 0, 43, 25, 29, 11, 26]), #sant

    City(5, [37, 46, 43, 10, 43, 0, 19, 45, 47, 43]), #bog

    City(6, [32, 33, 36, 27, 25, 19, 0, 38, 31, 35]), #lima

    City(7, [9, 11, 3, 45, 29, 45, 38, 0, 20, 3]), #rj

    City(8, [23, 8, 22, 51, 11, 47, 31, 20, 0, 17]), #ba

    City(9, [9,  8, 5, 44, 26, 43, 35, 3, 17, 0]) #sp
]
