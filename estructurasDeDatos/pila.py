class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0


    def peek(self):
        if not self.is_empty():
            item = self.items[-1]
            return item, hex(id(item))  # valor y dirección en hexadecimal
        return None, None

    def zise(self):
        length = len(self.items)
        return length, hex(id(self.items))  # tamaño y dirección de la lista interna

    def buscar(self, valor):
        return valor in self.items