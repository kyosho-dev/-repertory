class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class Stack:
    def __init__(self): # cria a lista sem elemento
        self.top = None
        self._size = 0


    def push(self,elen): 
        node = Node(elen)
        node.next = self.top
        self.top = node
        self._size = self._size + 1
        node.data = elen

    def pop(self):
        if self.empty():
            return 'pilha vazia'
        node = self.top
        self.top = self.top.next
        self._size -= 1
        return node.data
   
    def __repr__(self):
        if self._size == 0:
            return 'pilha vazia'
        s = ''
        p = self.top
        while(p):
            s += str(p.data) + '\n'
            p = p.next
        return s
    
    def Size(self):
        return self._size

pilha = Stack()
pilha.push(1)
pilha.push(5)
pilha.push(10)

print(pilha._size)