class Nodo:
    def __init__(self, key, value):
        self.id = key
        self.value = value
        self.connectedTo = {}
        
    def addNeighbor(self, nbr, relationType):
        try: # Caso já tenha relação com o nodo, adicionar a nova
          self.connectedTo[nbr]
          # if(relationType in self.connectedTo[nbr]): # Já possui a relação
          #   return True
          
          self.connectedTo[nbr].append(relationType)
        except: # Primeira relação. Criar lista e adicionar a string que descreve a relação
          self.connectedTo[nbr] = [relationType]  
        
        return True
    
    def getConnections(self):
        string = ''
        for i in self.connectedTo.keys():
          string += f'Relações do nodo {self.id} com o nodo {i}: {self.connectedTo[i]}\n'
        
        # Retorna o dicionário contendo todas as relações do nodo e uma string interpolada
        return self.connectedTo, string  
    
    def getId(self):
        return self.id
    
    def getValue(self):
        return self.value
    
    def getRelations(self, nbr):
        return self.connectedTo[nbr] # Retorna as relações com um nodo em específico
  
    def __iter__(self):
      for key in self.connectedTo.keys():
        yield key, self.connectedTo[key]

    # def __str__(self):
    #     return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
    