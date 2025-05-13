from graphviz import Digraph

class Stack:
    def __init__(self):
        self.items = []

    def agregar(self, item):
        self.items.append(item)

    def eliminar(self):
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

    def visualize(self, filename='stack'):
        dot = Digraph(format='png')
        dot.attr(rankdir='TB')
        dot.node_attr.update(shape='box')

        for i, item in enumerate(reversed(self.items)):
            dot.node(str(i), str(item))
            if i>0:
                dot.edge(str(i-1), str(i))

        dot.render(filename, view=True)
