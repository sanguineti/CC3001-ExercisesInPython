# Recibe como parámetro una matriz (cuadrada) de n x n con los costos a(i,j) de ir desde
# un lugar i hasta otro lugar j sin pasar por puntos intermedios.
# Retorna una nueva matriz que contiene el costo óptimo C(i,j) utilizando programación dinámica,
# considerando paradas intermedias. Toma tiempo cúbico.
# optimal = np.zeros((n, n), dtype=int)

import numpy as np 
def costo_minimo(matriz):
    n = len(matriz)
    for i in range(0, n):
        for j in range(1, n):
            opti = matriz[i][j]
            for k in range(i, j - i + 1):
                opti = min(matriz[i][k] + matriz[k][j], opti)
            matriz[i][j] = opti
    return matriz

if __name__=="__main__":
    test = [[0, 6, 9, 7], [0, 0, 2, 15], [0, 0, 0, 3], [0, 0, 0, 0]]
    a = costo_minimo(test)
    print(a)