from PyQt6.QtWidgets import QWidget, QMessageBox, QApplication
from PyQt6 import uic

class InterfazInformacion(QWidget):
    def __init__(self, estructura_instancia, tipo_dato):
        super().__init__()
        uic.loadUi("vistas/informacion.ui", self)
        self.setFixedSize(400, 373)

        valor_nodo_primero, direccion_nodo_primero = estructura_instancia.peek()
        tamanio_cantidad_nodo, direccion_cantidad_nodo = estructura_instancia.zise()

        self.nodo_primero.setText(str(valor_nodo_primero))
        self.nodo_primero_direccion.setText(str(direccion_nodo_primero))

        self.cantidad_nodo.setText(str(tamanio_cantidad_nodo))
        self.cantidad_nodo_direccion.setText(str(direccion_cantidad_nodo))

        self.titulo_info.setText("Pilas")
        self.tipo_dato.setText(tipo_dato)

        self.nodo_ultimo_valor.setText("0")