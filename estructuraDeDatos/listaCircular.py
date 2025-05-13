from graphviz import Digraph

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

    @property
    def dato(self):
        return self.__dato

    @dato.setter
    def dato(self, nuevo_dato):
        self.__dato = nuevo_dato

class ListaDobleCircular:
    def __init__(self):
        self.primero = None
        self.actual = None
        self.contador = 0

    def insertar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.primero:
            nuevo_nodo.siguiente = nuevo_nodo.anterior = nuevo_nodo
            self.primero = self.actual = nuevo_nodo
        else:
            ultimo = self.primero.anterior
            nuevo_nodo.siguiente = self.primero
            nuevo_nodo.anterior = ultimo
            self.primero.anterior = ultimo.siguiente = nuevo_nodo
            self.primero = self.actual = nuevo_nodo
        self.contador += 1

    def insertar_final(self, dato):
        if not self.primero:
            self.insertar_inicio(dato)
        else:
            ultimo = self.primero.anterior
            nuevo_nodo = Nodo(dato)
            nuevo_nodo.siguiente = self.primero
            nuevo_nodo.anterior = ultimo
            self.primero.anterior = ultimo.siguiente = nuevo_nodo
            self.actual = nuevo_nodo
            self.contador += 1

    def insertar_n_posicion(self, dato, posicion):
        if posicion <= 0:
            self.insertar_inicio(dato)
        elif posicion >= self.contador:
            self.insertar_final(dato)
        else:
            nuevo_nodo = Nodo(dato)
            actual = self.primero
            for _ in range(posicion - 1):
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            nuevo_nodo.anterior = actual
            actual.siguiente.anterior = nuevo_nodo
            actual.siguiente = nuevo_nodo
            self.contador += 1

    def eliminar_inicio(self):
        if not self.primero:
            return
        if self.primero.siguiente == self.primero:
            self.primero = None
        else:
            ultimo = self.primero.anterior
            self.primero = self.primero.siguiente
            self.primero.anterior = ultimo
            ultimo.siguiente = self.primero
        self.contador -= 1

    def eliminar_final(self):
        if not self.primero:
            return
        if self.primero.siguiente == self.primero:
            self.primero = None
        else:
            ultimo = self.primero.anterior
            penultimo = ultimo.anterior
            penultimo.siguiente = self.primero
            self.primero.anterior = penultimo
        self.contador -= 1

    def eliminar_n_posicion(self, posicion):
        if self.contador == 0 or posicion < 0 or posicion >= self.contador:
            return
        if posicion == 0:
            self.eliminar_inicio()
        elif posicion == self.contador - 1:
            self.eliminar_final()
        else:
            actual = self.primero
            for _ in range(posicion):
                actual = actual.siguiente
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior
            self.contador -= 1

    def rotar_izquierda(self):
        if self.primero:
            self.primero = self.primero.siguiente

    def rotar_derecha(self):
        if self.primero:
            self.primero = self.primero.anterior

    def mostrar_lista(self):
        if not self.primero:
            print("Lista vacía")
            return
        actual = self.primero
        for _ in range(self.contador):
            print(actual.dato, end=" <-> ")
            actual = actual.siguiente
        print(" (inicio)")

    def visualize(self, nombre_archivo="lista_doble_circular"):
        if not self.primero:
            print("La lista está vacía. No se puede graficar.")
            return

        dot = Digraph(comment="Lista Doble Circular", format="png")
        dot.attr(rankdir="LR", size="8")

        nodos = []
        enlaces = []

        actual = self.primero
        for i in range(self.contador):
            nodo_id = f"n{i}"
            nodos.append((nodo_id, actual.dato))
            actual = actual.siguiente

        # Agregar nodos al grafo
        for nodo_id, dato in nodos:
            dot.node(nodo_id, label=str(dato), shape="circle", style="filled", fillcolor="lightblue")

        # Enlaces dobles
        for i in range(len(nodos)):
            origen, _ = nodos[i]
            destino, _ = nodos[(i + 1) % len(nodos)]  # Circularidad
            dot.edge(origen, destino, dir="forward")
            dot.edge(destino, origen, dir="back")

        # Guardar y mostrar
        dot.render(nombre_archivo, view=True)

    def buscar(self, valor):
        if not self.primero:
            return False

        actual = self.primero
        encontrado = False

        # Recorremos la lista circular
        for _ in range(self.contador):
            if actual.dato == valor:
                encontrado = True
                break
            actual = actual.siguiente

        return encontrado




