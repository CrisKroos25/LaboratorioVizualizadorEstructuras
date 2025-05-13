from controles.informacion import *
from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6 import uic

class InterfazOpciones(QWidget):
    def __init__(self, tipo_dato, estructura, estructura_instancia):
        super().__init__()
        uic.loadUi("vistas/opciones.ui", self)
        self.setFixedSize(400, 373)

        self.tipo_dato = tipo_dato
        self.estructura = estructura
        self.estructura_instancia = estructura_instancia

        self.operaciones_por_estructura = {
            "pila": ["Insertar", "Eliminar", "Buscar valor", "Informacion", "Vizualizar estructura"],
            "cola": ["Insertar", "Eliminar", "Buscar valor", "Information", "Vizualizar estructura"],
            "lista circular": [
                "Insertar inicio", "Insertar final", "Eliminar inicio", "Eliminar final",
                "Buscar valor", "Rotar izquierda", "Rotar derecha", "Vizualizar estructura"
            ],
            # Más estructuras si es necesario
        }

        self.configurar_interfaz()

    def configurar_interfaz(self):
        self.box_operaciones.clear()
        self.box_operaciones.addItems(
            self.operaciones_por_estructura.get(self.estructura, ["No hay operaciones disponibles"])
        )
        self.opciones_titulo.setText(self.estructura)
        self.btnEjecutar.clicked.connect(self.realizar_operacion)

    def realizar_operacion(self):
        operacion = self.box_operaciones.currentText()
        valor = self.input_valor.text()
        self.input_valor.clear()

        # Operaciones sin valor necesario
        if operacion in ["Eliminar", "Informacion", "Vizualizar estructura"]:
            self.operar_sin_valor(operacion)
            return

        # Intentar convertir valor al tipo de dato correspondiente
        valor = self.convertir_valor(valor)
        if valor is None:
            return  # Ya se mostró mensaje de error

        # Operaciones con valor
        if self.estructura in ["pila", "cola"]:
            self.operar_pila_cola(operacion, valor, self.estructura)
        elif self.estructura == "lista circular":
            self.operar_lista_circular(operacion, valor, self.estructura)

    def convertir_valor(self, valor):
        try:
            if self.tipo_dato == "numero entero":
                return int(valor)
            elif self.tipo_dato == "numero flotante":
                return float(valor)
            elif self.tipo_dato == "cadena de texto":
                return str(valor)
            elif self.tipo_dato == "booleano":
                if valor.lower() in ["true", "false"]:
                    return valor.lower() == "true"
                else:
                    raise ValueError("Valor booleano inválido")
        except ValueError:
            self.mostrar_mensaje(f"Valor inválido para {self.tipo_dato}")
            return None

    def operar_sin_valor(self, operacion):
        if operacion == "Eliminar":
            if self.estructura == "pila" or "cola":
                self.estructura_instancia.eliminar()
                self.mostrar_mensaje("Valor eliminado correctamente")
        elif operacion == "Informacion":
            self.informacion = InterfazInformacion(self.estructura_instancia, self.tipo_dato)
            self.informacion.show()
        elif operacion == "Vizualizar estructura":
            self.estructura_instancia.visualize()

    def operar_pila_cola(self, operacion, valor, estructura):
        if operacion == "Insertar":
            self.estructura_instancia.agregar(valor)
            self.mostrar_mensaje("Valor agregado correctamente")
        elif operacion == "Buscar valor":
            encontrado = self.estructura_instancia.buscar(valor)
            self.mostrar_mensaje(
                f"Valor {valor} {'encontrado' if encontrado else 'no existe'} dentro de la {estructura}."
            )

    def operar_lista_circular(self, operacion, valor, estructura):
        if operacion == "Insertar inicio":
            self.estructura_instancia.insertar_inicio(valor)
            self.mostrar_mensaje("Valor agregado correctamente")
        elif operacion == "Insertar final":
            self.estructura_instancia.insertar_final(valor)
            self.mostrar_mensaje("Valor agregado correctamente")
        elif operacion == "Buscar valor":
            encontrado = self.estructura_instancia.buscar(valor)
            self.mostrar_mensaje(
                f"Valor {valor} {'encontrado' if encontrado else 'no existe'} dentro de la {estructura}." )

    def mostrar_mensaje(self, texto):
        QMessageBox.information(self, "Resultado", texto)
