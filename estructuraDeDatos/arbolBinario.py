from collections import deque

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        if not self.raiz:
            self.raiz = Nodo(valor)
        else:
            cola = deque([self.raiz])
            while cola:
                nodo = cola.popleft()
                if not nodo.izquierda:
                    nodo.izquierda = Nodo(valor)
                    return
                else:
                    cola.append(nodo.izquierda)
                if not nodo.derecha:
                    nodo.derecha = Nodo(valor)
                    return
                else:
                    cola.append(nodo.derecha)

    def buscar(self, valor):
        if not self.raiz:
            return None
        cola = deque([self.raiz])
        while cola:
            nodo = cola.popleft()
            if nodo.valor == valor:
                return nodo
            if nodo.izquierda:
                cola.append(nodo.izquierda)
            if nodo.derecha:
                cola.append(nodo.derecha)
        return None

    def eliminar(self, valor):
        if not self.raiz:
            return

        if self.raiz.valor == valor and not self.raiz.izquierda and not self.raiz.derecha:
            self.raiz = None
            return

        cola = deque([self.raiz])
        nodo_a_eliminar = None
        ultimo = None
        padre_ultimo = None

        while cola:
            nodo = cola.popleft()
            if nodo.valor == valor:
                nodo_a_eliminar = nodo
            if nodo.izquierda:
                padre_ultimo = nodo
                cola.append(nodo.izquierda)
            if nodo.derecha:
                padre_ultimo = nodo
                cola.append(nodo.derecha)
            ultimo = nodo

        if nodo_a_eliminar:
            nodo_a_eliminar.valor = ultimo.valor
            if padre_ultimo:
                if padre_ultimo.derecha == ultimo:
                    padre_ultimo.derecha = None
                elif padre_ultimo.izquierda == ultimo:
                    padre_ultimo.izquierda = None

    def visualizar(self):
        def _imprimir_arbol(nodo, prefijo="", es_izquierda=True):
            if nodo:
                print(prefijo + ("└── " if es_izquierda else "┌── ") + str(nodo.valor))
                if nodo.izquierda or nodo.derecha:
                    if nodo.derecha:
                        _imprimir_arbol(nodo.derecha, prefijo + ("    " if es_izquierda else "│   "), False)
                    if nodo.izquierda:
                        _imprimir_arbol(nodo.izquierda, prefijo + ("    " if es_izquierda else "│   "), True)

        _imprimir_arbol(self.raiz)

