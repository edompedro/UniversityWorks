# -*- coding: utf-8 -*-
from Nodo import *
class Graph:
    def __init__(self):
        self.vertList = {}  #lista de nodos
        self.numVertices = 0
        
    def addNodo(self, key, value):
        self.numVertices = self.numVertices + 1
        newVertex = Nodo(key, value)
        self.vertList[key] = newVertex  #a key do nodo é a chave dele no json/dic
        return newVertex
    
    def getNodo(self, key):
        if key in self.vertList:
            return self.vertList[key]  #retorna todos os verticies q tem conexão com o nodo informado
        else:
            return None
    
    def __contains__(self, key):
        return key in self.vertList
    
    def addEdge(self, f, t, type, weight=0):
        if(f in self.vertList and t in self.vertList):
            if(type == "bidirecional"):     #relação bidirecional
                self.vertList[f].addNeighbor(self.vertList[t].getId(), weight)  
                self.vertList[t].addNeighbor(self.vertList[f].getId(), weight)  
            else: self.vertList[f].addNeighbor(self.vertList[t].getId(), weight)  #adiciona a relacao unilateral

    #pra ficar bilateral temos que duplicar a linha invertendo, quando quiser fazer mais relações só
    #chamar essa função de novo com os "pesos" diferentes
    def getVertices(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())