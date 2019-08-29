import sys
import math

class NodoArbolBinario:
    def __init__(self, v, izq = None, der = None):
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
            return -sys.maxsize - 1 
        return max(arbol.valor, max(max(arbol.izq), max(arbol.der)))