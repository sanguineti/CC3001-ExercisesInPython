import numpy as np


def subarreglo_maximo(arreglo, i, j):
    # caso base, si es que el arreglo es de largo 1, el máximo es el elemento solo.
    if i == j:
        return arreglo[0]
    m = (j + i) // 2
    suma_max_izq = subarreglo_maximo(arreglo, i, m)
    suma_max_der = subarreglo_maximo(arreglo, m + 1, j)

    max_i = 0
    max_d = 0

    suma = 0
    x = m

    while x >= i:
        suma += arreglo[x]
        if suma > max_i:
            max_i = suma
        x -= 1

    suma = 0
    x = m + 1

    while x <= j:
        suma += arreglo[x]
        if suma > max_d:
            max_d = suma
        x += 1

    return max(max_d + max_i, max(suma_max_der, suma_max_izq))


arreglo_prueba = np.array([-2, 5, 7, -1, 4, -3, 2, -10])
print(subarreglo_maximo(arreglo_prueba, 0, arreglo_prueba.size - 1))
