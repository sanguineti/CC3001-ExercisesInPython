import sys
import numpy as np

MIN_VALUE = -sys.maxsize - 1


def segmento_maximo(arreglo):
    suma_maxima = MIN_VALUE
    indice_inicio = -1
    indice_fin = -1

    # invariante: se conoce el segmento de suma máxima que comienza en un índice menor a i
    for i in range(len(arreglo)):
        # invariante: se conoce el segmento de suma máxima que comienza en el i actual y termina en un indice
        # anterior a j

        for j in range(i, len(arreglo)):
            suma = 0
            # para cada iteración se suma el rango completo
            for k in range(i, j + 1):
                suma += arreglo[k]
            if suma > suma_maxima:
                suma_maxima = suma
                indice_inicio = i
                indice_fin = j
    print("Suma máxima = ", suma_maxima)
    print("Índice inicio = ", indice_inicio)
    print("Indice fin = ", indice_fin, "\n")


def segmento_maximo_2(arreglo):
    suma_maxima = MIN_VALUE
    indice_inicio = -1
    indice_fin = -1
    # invariante: se conoce el segmento de suma máxima que comienza en un índice menor a i
    for i in range(len(arreglo)):
        suma_actual = 0

        for j in range(i, arreglo.size):
            # se ocupa la suma anterior para obtener la suma del rango actual
            suma_actual += arreglo[j]
            if suma_actual > suma_maxima:
                suma_maxima = suma_actual
                indice_inicio = i
                indice_fin = j
    print("Suma máxima = ", suma_maxima)
    print("Índice inicio = ", indice_inicio)
    print("Indice fin = ", indice_fin, "\n")


def segmento_maximo_3(arreglo):
    suma_maxima = MIN_VALUE
    indice_inicio_actual = 0
    indice_inicio = 0
    indice_fin = -1

    suma_actual = 0

    # invariante: se conoce el segmento de suma máxima que comienza en un índice menor a i
    for i in range(len(arreglo)):
        suma_actual += arreglo[i]

        if suma_actual > suma_maxima:
            suma_maxima = suma_actual
            indice_inicio = indice_inicio_actual
            indice_fin = i
        elif suma_actual < 0:
            suma_actual = 0
            indice_inicio_actual = i + 1

    print("Suma máxima = ", suma_maxima)
    print("Índice inicio = ", indice_inicio)
    print("Indice fin = ", indice_fin, "\n")


arreglo_prueba = np.array([1, 2, 3, -7, 2, 8, 50, -20, -100, 7, -1, -3, 0, 48, 10, 5])
segmento_maximo(arreglo_prueba)
segmento_maximo_2(arreglo_prueba)
segmento_maximo_3(arreglo_prueba)
