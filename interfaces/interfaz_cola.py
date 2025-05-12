from interfaces.base_estructura import BaseEstructuraInterfaz
from graphviz import Digraph
from controles.informacion import InterfazInformacion

class InterfazCola(BaseEstructuraInterfaz):
    def __init__(self, tipo_dato, estructura, estructura_instancia):
        super().__init__(tipo_dato, estructura, estructura_instancia, "vistas/opciones.ui")

    def insertar(self, valor):
        self.instancia.enqueue(valor)
        self.mostrar_mensaje("Valor agregado a la cola")

    def eliminar(self):
        try:
            valor = self.instancia.dequeue()
            self.mostrar_mensaje(f"Valor {valor} eliminado de la cola")
        except Exception as e:
            self.mostrar_mensaje(str(e))

    def buscar_valor(self, valor):
        if self.instancia.buscar(valor):
            self.mostrar_mensaje(f"Valor {valor} encontrado en la cola")
        else:
            self.mostrar_mensaje(f"Valor {valor} no encontrado en la cola")

    def mostrar_informacion(self):
        self.informacion = InterfazInformacion(self.instancia, self.tipo_dato)
        self.informacion.show()

    def visualizar(self):
        filename='queue'
        dot = Digraph(format='png')
        dot.attr(rankdir='TB')
        dot.node_attr.update(shape='box')

        for i, item in enumerate(reversed(self.instancia.items)):
            dot.node(str(i), str(item))
            if i > 0:
                dot.edge(str(i - 1), str(i))

        dot.render(filename, view=True)


