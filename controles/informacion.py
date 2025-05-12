from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox
from typing import Any, Tuple

class InterfazInformacion(QWidget):
    def __init__(self, estructura_instancia: Any, tipo_dato: str, tipo_estructura: str):
        super().__init__()
        uic.loadUi("vistas/informacion.ui", self)
        self.setFixedSize(400, 373)

        self.tipo_estructura = tipo_estructura.lower()
        self.estructura = estructura_instancia
        self.tipo_dato = tipo_dato

        self.configurar_ui()
        self.mostrar_informacion()

    def configurar_ui(self):
        """Configura los elementos estáticos de la UI"""
        self.titulo_info.setText(f"Información de {self.tipo_estructura.capitalize()}")
        self.tipo_dato_label.setText(f"Tipo de dato: {self.tipo_dato}")

        # Ocultar campos no relevantes inicialmente
        self.nodo_ultimo_valor.setVisible(False)
        self.label_ultimo_nodo.setVisible(False)
        self.nodo_ultimo_direccion.setVisible(False)

    def mostrar_informacion(self):
        """Muestra la información específica de cada estructura"""
        try:
            if self.tipo_estructura == "pila":
                self.mostrar_info_pila()
            elif self.tipo_estructura == "cola":
                self.mostrar_info_cola()
            elif self.tipo_estructura in ["lista enlazada simple", "lista circular", "lista doble enlazada"]:
                self.mostrar_info_lista()
            elif self.tipo_estructura in ["arbol binario", "arbol de busqueda"]:
                self.mostrar_info_arbol()
            else:
                raise ValueError(f"Estructura {self.tipo_estructura} no soportada")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"No se pudo obtener información: {str(e)}")

    def mostrar_info_pila(self):
        """Muestra información específica para pilas"""
        valor, direccion = self.estructura.peek()
        tamanio, dir_tamanio = self.estructura.size()

        self.nodo_primero.setText(str(valor))
        self.nodo_primero_direccion.setText(str(direccion))
        self.cantidad_nodo.setText(str(tamanio))
        self.cantidad_nodo_direccion.setText(str(dir_tamanio))

