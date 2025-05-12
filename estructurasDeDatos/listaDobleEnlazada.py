class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar_al_inicio(self, dato):
        nuevo_nodo = NodoDoble(dato)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo_nodo

        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

    def insertar_al_final(self, dato):
        nuevo_nodo = NodoDoble(dato)
        if self.cola is None: #Si la lista esta vacia
            self.cabeza = self.cola = nuevo_nodo

        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def eliminar_inicio(self):
        if self.cabeza is None:
            return
        if self.cabeza == self.cola:
            self.cabeza = self.cola = None
        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None

    def eliminar_final(self):
        if self.cola is None:
            return
        if self.cola == self.cabeza:
            self.cabeza = self.cola = None
        else:
            self.cola = self.cola.anterior
            self.cola.siguiente = None

    def recorrer_adelante(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" <->")
            actual = actual.siguiente
        print("None")

    def recorrer_atras(self):
        actual = self.cola
        while actual:
            print(actual.dato, end=" <->")
            actual = actual.anterior
        print("None")




