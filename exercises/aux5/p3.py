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
    def __init__(self, raiz=None):
        self.raiz = raiz

    @staticmethod
    def numero_nodos(arbol):
        if arbol.raiz == None:
            return 0
        return 1 + ArbolBinario.numero_nodos(arbol.der) + ArbolBinario.numero_nodos(arbol.izq)

    @staticmethod
    def maximo(arbol):
        if arbol.raiz == None:
            return MIN_VALUE
        return max(arbol.valor, max(ArbolBinario.maximo(arbol.izq), ArbolBinario.maximo(arbol.der)))

    @staticmethod
    def minimo(arbol):
        if arbol.raiz == None:
            return sys.maxsize
        return min(arbol.valor, min(ArbolBinario.minimo(arbol.izq), ArbolBinario.minimo(arbol.der)))

    @staticmethod
    def suma(arbol):
        if arbol.raiz == None:
            return 0
        return arbol.val + ArbolBinario.suma(arbol.izq) + ArbolBinario.suma(arbol.der)

    @staticmethod
    def pisos(arbol):
        if arbol.raiz == None:
            return 0
        return 1 + max(ArbolBinario.pisos(arbol.izq), ArbolBinario.pisos(arbol.der))

    @staticmethod
    def es_arbol_binario(arbol, min=MIN_VALUE, max=MAX_VALUE):
        if arbol.raiz == None:
            return True
        if arbol.raiz.val < min or arbol.raiz.val > max:
            return False
        return ArbolBinario.es_arbol_binario(arbol.raiz.izq, min, arbol.raiz.val) and ArbolBinario.es_arbol_binario(arbol.raiz.der, arbol.raiz.val, MAX_VALUE)


binario = NodoArbolBinario(5,
                           NodoArbolBinario(3,
                                            NodoArbolBinario(2),
                                            NodoArbolBinario(4)),
                           NodoArbolBinario(7,
                                            NodoArbolBinario(6),
                                            NodoArbolBinario(8,
                                                             None,
                                                             NodoArbolBinario(9))))
arbol_binario = ArbolBinario(binario)
print(ArbolBinario.es_arbol_binario(arbol_binario))