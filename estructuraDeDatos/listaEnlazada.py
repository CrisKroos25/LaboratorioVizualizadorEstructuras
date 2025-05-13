class Nodo:
    def __init__(self, dato):
        self.siguiente = None
        self.dato = dato

class ListaSimple:
    def __init__(self):
        self.cabeza = None

    def insertar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def insertar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo


    def eliminar_inicio(self):
        actual = self.cabeza
        self.cabeza = actual.siguiente

    def eliminar_final(self):
        actual = self.cabeza
        while actual.siguiente.siguiente:
            actual = actual.siguiente
        actual.siguiente = None

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=' -> ')
            actual = actual.siguiente
        print("None")

    def buscar(self, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                return actual.dato
            actual = actual.siguiente
        return None




