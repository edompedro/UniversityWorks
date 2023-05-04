# -*- coding: utf-8 -*-
from Grafo import Graph

grafo = Graph()

data = {"name": "Pedro",
        "idade": 21}
data1 = {"name": "joao",
        "idade": 21}
data2 = {"name": "thiago",
        "idade": 21}

grafo.addNodo(0,data)
grafo.addNodo(1,data1)
grafo.addNodo(2,data2)

grafo.addEdge(0,1,"direcional", 3)
grafo.addEdge(0,2,"bidirecional",1)

print(grafo.getNodo(0)) #retorna o nodo

print(grafo.getNodo(2).getConnectionsWeight(1)) #peso da conexão entre nodo 0 e 1
#getconnections printa o json onde a key é a chave e o valor dentro dela é o peso da conexão
