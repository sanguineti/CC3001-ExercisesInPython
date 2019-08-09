import numpy as np
def particion_lomuto(arreglo, ini, fin):
    pivote = arreglo[fin]
    i = ini
    for j in range(fin - ini - 1):
        if arreglo[j] <= pivote:
            arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
            i += 1
    arreglo[i], arreglo[fin] = arreglo[fin], arreglo[i]
    # print(arreglo)
    return i

a = np.array([7,2,1,8,6,3,5,4])
print(particion_lomuto(a, 0, 7))