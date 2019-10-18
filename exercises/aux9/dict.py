import numpy as np
import sys
MIN_VALUE = -sys.maxsize - 1

def ordernar_via_diccionario(arr):
    diccionario = DiccionarioOrdenado()
    for elemento in arr:
        diccionario.insert(elemento)
    arreglo = np.empty(len(arr), dtype=int)
    minimo = MIN_VALUE
    i = 0
    while diccionario.sucesor(minimo) != None:
        arreglo[i] = diccionario.sucesor(minimo)
        minimo = diccionario.sucesor(minimo)
    return arreglo     