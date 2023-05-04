# -*- coding: utf-8 -*-
from Nodo import *
class Graph:
    def __init__(self):
        self.nodoList = {}  #lista de nodos
        self.numVertices = 0
        self.listaDeRelacoesDoTipoConhecido = []
        self.listaDeRelacoesDoTipoAmigo = []
        self.listaDeRelacoesDoTipoParente = []
        self.listaDeRelacoesDoTipoCliente = []
    
    def hashByEmail(self, email):
        key = 0
        for i in email: key += ord(i)
        return key
        
    def addNodo(self, value):
        self.numVertices = self.numVertices + 1
        
        nodeKey = self.hashByEmail(value['email'])
        newNodo = Nodo(nodeKey, value)
        self.nodoList[nodeKey] = newNodo  #a key do nodo é a chave dele no json/dic
        return newNodo
    
    def getNodo(self, key):
        if key in self.nodoList:
            return self.nodoList[key]   # retorna um nodo, tomando como base a chave
        else:
            return None
    
    def __contains__(self, key):
        return key in self.nodoList
    
    def addEdge(self, f, t, relationType):
      if f in self.nodoList and t in self.nodoList:
        if relationType not in ['known', 'friend', 'relative', 'customer']:
          return False

        # Adiciona a relacao unilateral (somente conhecido)
        self.nodoList[f].addNeighbor(self.nodoList[t].getId(), relationType)  
        
        # Adiciona a relação contrária, se for de algum dos tipos abaixo
        if relationType in ['friend', 'relative', 'customer']: 
          self.nodoList[t].addNeighbor(self.nodoList[f].getId(), relationType)  


    def makeRelationsList(self):
        
         for nodoId1 in self.nodoList.keys():   
        #pega um nodo e na sequencia pega os nodos que estão ligados a ele
            for nodoId2 in self.nodoList[nodoId1].getConnections()[0].keys():
        #pega o id do nodo que ta conectado ao 1 nodo e cria a tupla da relação
                tuplaRelacao = (nodoId1, nodoId2)
                types = self.nodoList[nodoId1].getConnections()[0][nodoId2]    
        #vetor com os tipos de relações entre 2 nodos, pq podemos ter mais de 1 tipo de
        #relação entre dois nodos. Ex: known e friend
                for i in range(len(types)):
                    if(types[i] == 'friend'): 
                        self.listaDeRelacoesDoTipoAmigo.append(tuplaRelacao)
                    elif(types[i] == 'relative'):
                        self.listaDeRelacoesDoTipoParente.append(tuplaRelacao)
                    elif(types[i] == 'known'):
                        self.listaDeRelacoesDoTipoConhecido.append(tuplaRelacao)
                    elif(types[i] == 'customer'):
                        self.listaDeRelacoesDoTipoCliente.append(tuplaRelacao)
        #percorre o vetor com os tipos de relações entre os dois nodos e identifica qual
        #relação existe entre eles e guarda a tupla na lista correspondente à relação.       
        
        
    def getVertices(self):
        return self.nodoList.keys()
    
    def __iter__(self):
      for key in self.nodoList.keys():
        yield self.nodoList[key]