import sys
import math

MAX_VALUE = sys.maxsize
MIN_VALUE = -sys.maxsize - 1


class ArbolBinario:
    def __init__(self, v, izq=None, der=None):
        self.val = v
        self.izq = izq
        self.der = der

    @staticmethod
    def numero_nodos(arbol):
        if arbol == None:
            return 0
        return 1 + ArbolBinario.numero_nodos(arbol.der) + ArbolBinario.numero_nodos(arbol.izq)

    @staticmethod
    def maximo(arbol):
        if arbol == None:
            return MIN_VALUE
        return max(arbol.valor, max(ArbolBinario.maximo(arbol.izq), ArbolBinario.maximo(arbol.der)))

    @staticmethod
    def minimo(arbol):
        if arbol == None:
            return sys.maxsize
        return min(arbol.valor, min(ArbolBinario.minimo(arbol.izq), ArbolBinario.minimo(arbol.der)))

    @staticmethod
    def suma(arbol):
        if arbol == None:
            return 0
        return arbol.val + ArbolBinario.suma(arbol.izq) + ArbolBinario.suma(arbol.der)

    @staticmethod
    def pisos(arbol):
        if arbol == None:
            return 0
        return 1 + max(ArbolBinario.pisos(arbol.izq), ArbolBinario.pisos(arbol.der))

    @staticmethod
    def es_arbol_binario(arbol, min=MIN_VALUE, max=MAX_VALUE):
        if arbol == None:
            return True
        if arbol.val < min or arbol.val > max:
            return False
        return ArbolBinario.es_arbol_binario(arbol.izq, min, arbol.val) and ArbolBinario.es_arbol_binario(arbol.der, arbol.val, max)


binario = ArbolBinario(5,
                       ArbolBinario(3,
                                    ArbolBinario(2),
                                    ArbolBinario(4)),
                       ArbolBinario(7,
                                    ArbolBinario(6),
                                    ArbolBinario(8,
                                                 None,
                                                 ArbolBinario(9))))
no_binario = ArbolBinario(5,
                          ArbolBinario(3,
                                           ArbolBinario(2),
                                           ArbolBinario(16)),
                          ArbolBinario(8,
                                           ArbolBinario(7),
                                           ArbolBinario(9)))

# Casos de Prueba

# Es Binario
print(ArbolBinario.es_arbol_binario(binario))
print(ArbolBinario.es_arbol_binario(no_binario))
print(ArbolBinario.es_arbol_binario(None))

# Número de nodos
print("Número de nodos Ejemplo binario: ", ArbolBinario.numero_nodos(binario))
print("Número de nodos Ejemplo no binario: ", ArbolBinario.numero_nodos(no_binario))
print("Número de nodos Ejemplo nulo: ", ArbolBinario.numero_nodos(None))