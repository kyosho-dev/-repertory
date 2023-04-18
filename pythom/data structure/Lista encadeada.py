
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):  # cria a lista sem elemento
        self.top = None
        self._size = 0

    def append(self, elem):

        if self.top:
            # inserção quando a lista ja posui elementos
            pointer = self.top
            while (pointer.next):
                pointer = pointer.next

            pointer.next = Node(elem)  # o proximo elemento da lista

        else:
            self.top = Node(elem)  # sempre o primeiro elemento da lista
        self._size = self._size + 1

    def __len__(self):
        "retorna o tamanho da lista"
        # print(len(lista))

        return self._size

    def __getitem__(self, index):  # recupera um elemento
        # a = lista[6]
        pointer = self._getnode(index)
        if pointer:
            return pointer.data
        else:
            raise IndexError("list index out of range")

    def __setitem__(self, index, elem):
        # lista[5] = 9
        pointer = self._getnode(index)
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range")

    def set(self, index, elem):
        pass

    def _getnode(self, index):
        pointer = self.top
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")  # return None
        return pointer

    def index(self, elem):
        """Retorna o índice do elem na lista"""
        pointer = self.top
        i = 0
        while (pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i = i+1
        raise ValueError("{} is not in list".format(elem))

    def insert(self, index, elem):
        node = Node(elem)
        if index == 0:
            node.next = self.top
            self.top = node
        else:
            pointer = self._getnode(index-1)
            node.next = pointer.next
            pointer.next = node
        self._size = self._size + 1

    def remove(self, elem):
        if self.top == None:
            raise ValueError("{} is not in list".format(elem))
        elif self.top.data == elem:
            self.top = self.top.next
            self._size = self._size - 1
            return True
        else:
            ancestor = self.top
            pointer = self.top.next
            while (pointer):
                if pointer.data == elem:
                    ancestor.next = pointer.next
                    pointer.next = None
                    self._size = self._size - 1
                    return True
                ancestor = pointer
                pointer = pointer.next
        raise ValueError("{} is not in list".format(elem))

    def __repr__(self):
        r = ""
        pointer = self.top
        while (pointer):
            r = r + str(pointer.data) + "->"
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()


lista = Stack()

lista.append(7)
lista.append(2)
lista.append(3)

lista[0] = 10

print(lista[0])
