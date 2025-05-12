from PyQt6.QtWidgets import QWidget, QMessageBox
from graphviz import Digraph
from PyQt6 import uic

class BaseEstructuraInterfaz(QWidget):
    def __init__(self, tipo_dato, estructura, estructura_instancia, ui_path):
        super().__init__()
        uic.loadUi(ui_path, self)
        self.setFixedSize(400, 373)

        self.tipo_dato = tipo_dato
        self.estructura = estructura
        self.instancia = estructura_instancia

        self.setup_ui()
        self.connect_signals()

    def setup_ui(self):
        """Configuración inicial de la UI"""
        self.opciones_titulo.setText(self.estructura.capitalize())
        self.box_operaciones.addItems(self.get_operaciones_disponibles())

    def connect_signals(self):
        """Conectar señales y slots"""
        self.btnEjecutar.clicked.connect(self.realizar_operacion)

    def get_operaciones_disponibles(self):
        """Operaciones comunes a todas las estructuras"""
        return ["Insertar", "Eliminar", "Buscar valor", "Informacion", "Visualizar estructura"]

    def realizar_operacion(self):
        """Método base que delega a métodos específicos"""
        operacion = self.box_operaciones.currentText()
        valor = self.input_valor.text()

        try:
            valor = self.convertir_valor(valor)
        except ValueError as e:
            self.mostrar_mensaje(str(e))
            return

        if operacion == "Insertar":
            self.insertar(valor)
        elif operacion == "Eliminar":
            self.eliminar()
        elif operacion == "Buscar valor":
            self.buscar(valor)
        elif operacion == "Informacion":
            self.mostrar_informacion()
        elif operacion == "Visualizar estructura":
            self.visualizar()

    def convertir_valor(self, valor):
        """Convierte el valor al tipo de dato correspondiente"""
        if self.tipo_dato == "numero entero":
            return int(valor)
        elif self.tipo_dato == "numero flotante":
            return float(valor)
        elif self.tipo_dato == "booleano":
            if valor.lower() not in ["true", "false"]:
                raise ValueError("Ingresa 'True' o 'False' como valor booleano.")
            return valor.lower() == "true"
        return str(valor)  # Para cadena de texto y caracter


    def insertar(self, valor):
        """Método abstracto para insertar"""
        raise NotImplementedError

    def eliminar(self):
        """Método abstracto para eliminar"""
        raise NotImplementedError

    def buscar(self, valor):
        """Método abstracto para buscar"""
        raise NotImplementedError

    def mostrar_informacion(self):
        """Método abstracto para mostrar información"""
        raise NotImplementedError

    def visualizar(self):
        """Método abstracto para visualización gráfica"""
        raise NotImplementedError

    def mostrar_mensaje(self, texto):
        QMessageBox.information(self, "Resultado", texto)