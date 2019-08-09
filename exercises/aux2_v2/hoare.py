import numpy as np
def particion_hoare(arreglo, ini, fin):
    pivote = arreglo[0]
    i = ini
    j = fin + 1
    while True:

        while True:
            i += 1
            if not arreglo[i] < pivote:
                break
        while True:
            j -= 1
            if not arreglo[j] > pivote:
                break
        if i >= j:
            arreglo[0], arreglo[j] = arreglo[j], arreglo[0]
            # print(arreglo)
            return j
        
        arreglo[i], arreglo[j] = arreglo[j], arreglo[i]

# a = np.array([5,3,2,6,7,8,1,7,9])
a = np.array([3,7,2,4,8,6])
print(particion_hoare(a, 0, len(a)- 1))