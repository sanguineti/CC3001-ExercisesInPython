import sys
import math

MAX_VALUE = sys.maxsize
MIN_VALUE = -sys.maxsize - 1


class NodoArbolBinario:
    def __init__(self, v, izq=None, der=None):
        self.val = v
        self.izq = izq
        self.der = der


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def numero_nodos(self, arbol):
        if arbol.raiz == None:
            return 0
        return 1 + self.numero_nodos(arbol.der) + self.numero_nodos(arbol.izq)

    def maximo(self, arbol):
        if arbol.raiz == None:
            return MIN_VALUE
        return max(arbol.valor, max(self.maximo(arbol.izq), self.maximo(arbol.der)))

    def minimo(self, arbol):
        if arbol.raiz == None:
            return sys.maxsize
        return min(arbol.valor, min(self.minimo(arbol.izq), self.minimo(arbol.der)))

    def suma(self, arbol):
        if arbol.raiz == None:
            return 0
        return arbol.val + self.suma(arbol.izq) + self.suma(arbol.der)

    def pisos(self, arbol):
        if arbol.raiz == None:
            return 0
        return 1 + max(self.pisos(arbol.izq), self.pisos(arbol.der))

    def es_arbol_binario(self, arbol, min=MIN_VALUE, max=MAX_VALUE):
        if arbol.raiz == None:
            return True
        if arbol.valor < min or arbol.valor > max:
            return False
        return self.es_arbol_binario(arbol.raiz.izq, min, arbol.valor) and self.es_arbol_binario(arbol.raiz.der, arbol.raiz.val, MAX_VALUE)

binario = NodoArbolBinario(5,
        NodoArbolBinario(3,
                NodoArbolBinario(2),
                NodoArbolBinario(4)),
        NodoArbolBinario(7,
                NodoArbolBinario(6),
                NodoArbolBinario(8,
                    None,
                    NodoArbolBinario(9))))

