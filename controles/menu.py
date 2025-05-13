from estructuraDeDatos.pila import *
from estructuraDeDatos.cola import *
from estructuraDeDatos.listaCircular import *
from controles.opciones import *

class InterfazMenu(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("vistas/menu.ui", self)
        self.setFixedSize(400, 373)

        self.box_texto1.addItems(["numero entero", "numero flotante", "cadena de texto", "booleano" ])
        self.box_texto2.addItems(["pila", "cola", "lista enlazada simple", "lista circular", "lista doble enlazada"
                                  , "arbol binario", "arbol de busqueda"])

        self.pila = None
        self.cola = None
        self.lista_enlazada = None
        self.lista_circular = None
        self.lista_doble_enlazada = None
        self.arbol_binario = None
        self.arbol_de_busqueda = None

        self.boton_aceptar.clicked.connect(self.abrir_opciones)

    def procesar_seleccion(self):
        tipo_dato = self.box_texto1.currentText()
        estructura = self.box_texto2.currentText()

        return tipo_dato, estructura

    def mostrar_mensaje(self, texto):
        QMessageBox.information(self, "Resultado", texto)

    def abrir_opciones(self):
        tipo_dato, estructura = self.procesar_seleccion()

        if estructura == "pila":
            self.pila = Stack()
            self.opciones = InterfazOpciones(tipo_dato, estructura, self.pila)
            self.opciones.show()
        elif estructura == "cola":
            self.cola = Queue()
            self.opciones = InterfazOpciones(tipo_dato, estructura, self.cola)
            self.opciones.show()
        elif estructura == "lista circular":
            self.lista_circular = ListaDobleCircular()
            self.opciones = InterfazOpciones(tipo_dato, estructura, self.lista_circular)
            self.opciones.show()
        else:
            self.mostrar_mensaje("Estructura no implementada aún.")
