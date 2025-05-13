from graphviz import Digraph

class Queue:
    def __init__(self):
        self.items = []

    def agregar(self, item):
        self.items.append(item)

    def eliminar(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def zise(self):
        return len(self.items)

    def buscar(self, valor):
        return valor in self.items

    def visualize(self, filename='queue'):
        dot = Digraph(format='png')
        dot.attr(rankdir='TB')
        dot.node_attr.update(shape='box')

        for i, item in enumerate(reversed(self.items)):
            dot.node(str(i), str(item))
            if i>0:
                dot.edge(str(i-1), str(i))

        dot.render(filename, view=True)
