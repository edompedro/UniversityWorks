
class Nodo:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.father = None
    
    def insert_child(self,valor):
        nodo = Nodo(valor)
        if(nodo.value < self.value and self.left == None): 
            self.left = nodo
            nodo.father = self
        elif(nodo.value < self.value and self.left != None): self.left.insert_child(nodo.value)
        elif(nodo.value > self.value and self.right == None): 
            self.right = nodo
            nodo.father = self
        elif(nodo.value > self.value and self.right != None): self.right.insert_child(nodo.value)

    def search(self, valor):
        if(self.value == valor): 
            print("Valor encontrado", self.value)
            return self
        elif(self.left != None and valor < self.value): 
            newnodo = self.left
            return newnodo.search(valor)  
        elif(self.right != None and valor > self.value):
            newnodo = self.right
            return newnodo.search(valor)  
        else: 
            print("valor nao encontrado")
            
        
    def remove(self, valor):
        nodo = self.search(valor)
        if(nodo.right == None and nodo.left == None and nodo.father.left.value == nodo.value):
            nodo.father.left = None
        if(nodo.right == None and nodo.left == None and nodo.father.right.value == nodo.value):
            nodo.father.right = None
        elif(nodo.right == None and nodo.father.left.value == nodo.value): 
            nodo.father.left = nodo.left
            nodo.left.father = nodo.father
        elif(nodo.right != None and nodo.father.left.value == nodo.value):
            newnodo = nodo.right
            while newnodo.left != None:
                newnodo = newnodo.left
            newnodo.father.left = None
            newnodo.father = nodo.father
            nodo.father.left = newnodo
            newnodo.left = nodo.left
            newnodo.right = nodo.right
        elif(nodo.right != None and nodo.father.right.value == nodo.value):
            newnodo = nodo.right
            while newnodo.left != None:
                newnodo = newnodo.left
            newnodo.father.right = None
            newnodo.father = nodo.father
            nodo.father.right = newnodo
            newnodo.left = nodo.left
            newnodo.right = nodo.right
