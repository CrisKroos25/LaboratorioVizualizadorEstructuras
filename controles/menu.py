from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox, QApplication
from estructurasDeDatos.pila import *
from estructurasDeDatos.cola import *
from controles.opciones import *
from interfaces.interfaz_pila import *
from interfaces.interfaz_cola import *

class InterfazMenu(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("vistas/menu.ui", self)
        self.setFixedSize(400, 373)

        self.box_texto1.addItems([
            "numero entero", "numero flotante",
            "cadena de texto", "booleano",
            "caracter",
        ])
        self.box_texto2.addItems([
            "pila", "cola", "lista enlazada simple",
            "lista circular", "lista doble enlazada",
            "arbol binario", "arbol de busqueda"
        ])

        self.estructuras = {
            "pila": Stack,
            "cola": Queue

        }

        self.boton_aceptar.clicked.connect(self.abrir_opciones)

    def procesar_seleccion(self):
        tipo_dato = self.box_texto1.currentText()
        estructura = self.box_texto2.currentText()

        return tipo_dato, estructura

    def abrir_opciones(self):
        tipo_dato = self.box_texto1.currentText()
        estructura = self.box_texto2.currentText()

        if estructura not in self.estructuras:
            self.mostrar_mensaje("Estructura no implementada aún.")
            return

        # Crear instancia de la estructura
        instancia = self.estructuras[estructura]()

        # Obtener la interfaz correspondiente
        if estructura == "pila":
            self.opciones = InterfazPila(tipo_dato, estructura, instancia)
        elif estructura == "cola":
            self.opciones = InterfazCola(tipo_dato, estructura, instancia)

        self.opciones.show()

    def mostrar_mensaje(self, texto):
        QMessageBox.information(self, "Resultado", texto)










