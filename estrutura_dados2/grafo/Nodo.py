class Nodo:
    def __init__(self, key, value):
        self.id = key
        self.value = value
        self.connectedTo = {}
        
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight  #adiciona um vizinho
    
    def getConnections(self):
        return self.connectedTo.keys()  #retorna as conexões que o nodo possui
    
    def getConnectionsWeight(self, nodoId):
        if(nodoId in self.connectedTo.keys()): return(self.connectedTo[nodoId])    #retorna o peso da conexão entre um nodo e o outro
        else: return "No connection"
    
    def getId(self):
        return self.id
    
    def getValue(self):
        return self.value
    
    def getWeight(self, nbr):
        return self.connectedTo[nbr]
    
    # def __str__(self):
    #    return str(self.value["name"]) + ' connectedTo: ' + str([x for x in self.connectedTo])
    