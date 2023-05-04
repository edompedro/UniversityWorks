

class Obj:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.previous = None

class List:
    def __init__(self) -> None:
        self.start = None

    def insert(self, value, position):

        if(position > 0):
            obj = Obj(value)
            print(obj)
            if(position == 1):
                obj.next = self.start
                self.start = obj
            # else:
            #     aux = self.start #obj p
            #     for i in range(1,position-1): 
            #         if(aux.next != None): aux = aux.next      
            #     obj.next = aux.next
            #     obj.previous = aux
            #     aux1 = aux.next
            #     if(aux1 != None): aux1.previous = obj
            #     aux.next = obj
            #     aux.previous = aux.previous

    def imprime(self):
        obj = self.start
        while(obj != None):
            print(obj.data)
            obj = obj.next

    def remove(self,position):
        if(position == 1):
            self.start = self.start.next
        else:
            aux = self.start
            for i in range(1,position-1):
                aux = aux.next #q
            aux2 = aux.next #z
            aux.next = aux2.next
            aux2.next.previous = aux
            aux2.next = None

    def position(self, value):
        aux1 = self.start
        aux = aux1.data["id"]
        c = 1
        while(aux1 != None):
            if(aux == value):
                print("position:",aux)
                break
            else:
                aux1 = aux1.next
                aux = aux1.data["id"]
            c = c + 1

    def value(self, position):
        aux = self.start
        c = 1
        while(c < position):
            aux = aux.next
            c = c + 1
        print("Value:", aux.data)

    def destroy(self):
        aux = self.start
        while(aux != None):
            self.remove(1)
            aux = aux.next
        print("Lista destruida com sucesso!")
                


   