from interfaces.base_estructura import BaseEstructuraInterfaz
from controles.informacion import InterfazInformacion
from graphviz import Digraph


class InterfazPila(BaseEstructuraInterfaz):
    def __init__(self, tipo_dato, estructura, estructura_instancia):
        super().__init__(tipo_dato, estructura, estructura_instancia, "vistas/opciones.ui")

    def insertar(self, valor):
        self.instancia.push(valor)
        self.mostrar_mensaje("Valor agregado correctamente")

    def eliminar(self):
        try:
            self.instancia.pop()
            self.mostrar_mensaje("Valor eliminado correctamente")
        except Exception as e:
            self.mostrar_mensaje(str(e))

    def buscar(self, valor):
        if self.instancia.buscar(valor):
            self.mostrar_mensaje(f"Valor {valor} encontrado en la pila")
        else:
            self.mostrar_mensaje(f"Valor {valor} no encontrado en la pila")

    def mostrar_informacion(self):
        self.informacion = InterfazInformacion(self.instancia, self.tipo_dato)
        self.informacion.show()

    def visualizar(self):
        filename = 'stack'
        dot = Digraph(format='png')
        dot.attr(rankdir='TB')
        dot.node_attr.update(shape='box')

        for i, item in enumerate(reversed(self.instancia.items)):
            dot.node(str(i), str(item))
            if i > 0:
                dot.edge(str(i - 1), str(i))

        dot.render(filename, view=True)