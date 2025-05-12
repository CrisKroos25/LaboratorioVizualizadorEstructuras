class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBusquedaBinaria:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.izquierda = self._insertar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._insertar_recursivo(nodo.derecha, valor)
        return nodo

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None or nodo.valor == valor:
            return nodo
        if valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        else:
            return self._buscar_recursivo(nodo.derecha, valor)

    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo, valor):
        if nodo is None:
            return nodo
        if valor < nodo.valor:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, valor)
        else:
            # Caso 1: Sin hijos
            if nodo.izquierda is None and nodo.derecha is None:
                return None
            # Caso 2: Un hijo
            elif nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            # Caso 3: Dos hijos
            sucesor = self._minimo(nodo.derecha)
            nodo.valor = sucesor.valor
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, sucesor.valor)
        return nodo

    def _minimo(self, nodo):
        while nodo.izquierda:
            nodo = nodo.izquierda
        return nodo

    def visualizar(self):
        self._visualizar_recursivo(self.raiz)

    def _visualizar_recursivo(self, nodo, espacio=0, nivel=4):
        if nodo is None:
            return
        espacio += nivel
        self._visualizar_recursivo(nodo.derecha, espacio)
        print()
        print(" " * (espacio - nivel) + f"{nodo.valor}")
        self._visualizar_recursivo(nodo.izquierda, espacio)

