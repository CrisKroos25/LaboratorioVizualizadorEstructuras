from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox, QApplication
from graphviz import Digraph
from controles.informacion import *

class InterfazOpciones(QWidget):
    def __init__(self, tipo_dato, estructura, estructura_instancia):
        super().__init__()
        uic.loadUi("vistas/opciones.ui", self)
        self.setFixedSize(400, 373)

        self.tipo_dato = tipo_dato
        self.estructura = estructura
        self.estructura_instancia = estructura_instancia

        self.box_operaciones.addItems(["Insertar", "Eliminar", "Buscar valor", "Informacion", "Vizualizar estructura"])

        self.btnEjecutar.clicked.connect(self.realizar_operacion)
        self.input_valor.clear()

    def realizar_operacion(self):
        operacion = self.box_operaciones.currentText()
        valor = self.input_valor.text()

        if self.tipo_dato == "numero entero":
            try:
                valor = int(valor)
            except ValueError:
                self.mostrar_mensaje("Valor inválido para entero")
                return
        elif self.tipo_dato == "numero flotante":
            try:
                valor = float(valor)
            except ValueError:
                self.mostrar_mensaje("Valor inválido para flotante")
                return
        elif self.tipo_dato == "cadena de texto":
            try:
                valor = str(valor)
            except ValueError:
                self.mostrar_mensaje("Valor inválido para cadena de texto")
                return
        elif self.tipo_dato == "booleano":
            if valor.lower() in ["true", "false"]:
                valor = valor.lower() == "true"
            else:
                self.mostrar_mensaje("Ingresa 'True' o 'False' como valor booleano.")
                return

        if self.estructura == "pila":
            self.opciones_titulo.setText("pila")
            if operacion == "Insertar":
                self.estructura_instancia.push(valor)
                self.mostrar_mensaje("Valor agregado correctamente")
            elif operacion == "Eliminar":
                self.estructura_instancia.pop()
                self.mostrar_mensaje("Valor eliminado correctamente")
            elif operacion == "Buscar valor":
                if self.estructura_instancia.buscar_valor(valor):
                    self.mostrar_mensaje(f"Valor {valor} encontrado dentro de la pila.")
                else:
                    self.mostrar_mensaje(f"Valor {valor} no se existe dentro de la pila.")
            elif operacion == "Informacion":
                self.informacion = InterfazInformacion(self.estructura_instancia, self.tipo_dato)
                self.informacion.show()
            elif operacion == "Vizualizar estructura":
                filename='stack'
                dot = Digraph(format='png')
                dot.attr(rankdir='TB')
                dot.node_attr.update(shape='box')

                for i, item in enumerate(reversed(self.estructura_instancia.items)):
                    dot.node(str(i), str(item))
                    if i > 0:
                        dot.edge(str(i - 1), str(i))

                dot.render(filename, view=True)

    def mostrar_mensaje(self, texto):
        QMessageBox.information(self, "Resultado", texto)
