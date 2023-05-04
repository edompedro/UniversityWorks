# -*- coding: utf-8 -*-
from Grafo import Graph

grafo = Graph()
data = {
  "name": "Pedro",
  "idade": 21,
  "email": "pedro@social.com"
}

data1 = {
  "name": "joao",
  "idade": 21,
  "email": "joao@social.com"
}

data2 = {
  "name": "thiago",
  "idade": 21,
  "email": "thiago@social.com"
}

id0 = grafo.addNodo(data).id
id1 = grafo.addNodo(data1).id
id2 = grafo.addNodo(data2).id

grafo.addEdge(id0,id1,'friend')
grafo.addEdge(id0,id1,'relative')
grafo.addEdge(id0,id2,'relative')
grafo.addEdge(id1,id2,'known')

# O método getConnections() retorna uma tupla de tamanho 2
# Na 1ª posição, há o dicionário com todos as relações do nodo
# Na 2ª posição, há uma string que mostrar as relações em si

print(grafo.getNodo(id0).getConnections()[0].keys())   
grafo.makeRelationsList()   #cria as listas de relações do grafo, tendo a lista dps é "só" plotar 
print(grafo.listaDeRelacoesDoTipoParente, grafo.listaDeRelacoesDoTipoAmigo,
      grafo.listaDeRelacoesDoTipoCliente, grafo.listaDeRelacoesDoTipoConhecido)

'''
  COMO PRECISAMOS MONTAR AS LISTAS PARA PLOTAR O GRAFO

  1. São necessárias 4 lista, pois há 4 tipos de relações
  2. Precisamos percorrer todos os nodos do grafo
  3. Percorrer cada nodo que se relaciona com cada nodo do item 2.
  4. Separar em uma das 4 listas a relação, de acordo com o tipo da mesma
'''
'''
# 1. Criar as 4 listas
listaDeRelacoesDoTipoConhecido = []
listaDeRelacoesDoTipoAmigo = []
listaDeRelacoesDoTipoParente = []
listaDeRelacoesDoTipoCliente = []

# 2. Percorer todos os nodos 
for nodo in grafo: # 'nodo' é uma referência para cada nodo do grafo

  # 3. Percorrer cada nodo que se relaciona com cada 'nodo' (da linha 51)
  for connectedToList in nodo: 
    nodoOrigemId = nodo.id
    nodoDestinoId, listaDeRelacoes = connectedToList

    tuplaRelacao = (nodoOrigemId, nodoDestinoId)

    # 4. Separar as relações em uma das 4 listas
    if('known' in listaDeRelacoes):
      listaDeRelacoesDoTipoConhecido.append(tuplaRelacao)
    
    if('friend' in listaDeRelacoes):
      listaDeRelacoesDoTipoAmigo.append(tuplaRelacao)

    if('relative' in listaDeRelacoes):
      listaDeRelacoesDoTipoParente.append(tuplaRelacao)

    if('customer' in listaDeRelacoes):
      listaDeRelacoesDoTipoCliente.append(tuplaRelacao)

print(f'Id Pedro: {id0}')
print(f'Id Joao: {id1}')
print(f'Id Thiago: {id2}\n')

print('Arestas do tipo conhecido', listaDeRelacoesDoTipoConhecido)
print('Arestas do tipo amigo', listaDeRelacoesDoTipoAmigo)
print('Arestas do tipo parente', listaDeRelacoesDoTipoParente)
print('Arestas do tipo cliente', listaDeRelacoesDoTipoCliente)
'''