import numpy as np


# queremos chequear que la posición en donde queremos poner a la reina es segura
def es_seguro(tablero, x, y):
    #  revisamos si hay alguna otra reina en esta fila, no es necesario revisar la columna
    #  ya que estamos poniendo solo 1 reina por columna al distribuirlas.
    for i in range(y):  # invariante i = 0, i < y
        if tablero[x][i] == 1:
            return False
    # // revisamos si hay alguna otra reina en la diagonal creciente
    i = x
    j = y
    while i >= 0 and j >= 0:
        if tablero[i][j] == 1:
            return False
        i -= 1
        j -= 1
    # // revisamos si hay alguna otra reina en la diagonal decreciente
    i = x
    j = y
    while i < len(tablero) and j >= 0:
        if tablero[i][j] == 1:
            return False
        i += 1
        j -= 1
    # cualquier otro caso es seguro poner a la reina en x,y
    return True


# función recursiva que ubica a las reinas en el tablero o retorna false si no se pueden ubicar

def ubicar_reinas(tablero, col):
    # si col es igual a N quiere decir que ya hemos cubierto todo el tablero
    if col == len(tablero):
        return True
    # chequeamos si podemos poner a la reina en esta cada fila de col
    for i in range(0, len(tablero)):  # i < len(tablero)
        # primero debemos ver si el lugar que queremos ocupar es seguro
        if es_seguro(tablero, i, col):
            # de ser ubicamos a la reina en esta posición
            tablero[i][col] = 1
            # si podemos ubicar todas las otras reinas retornamos true
            if ubicar_reinas(tablero, col + 1):
                return True
            # si no, debemos cambiar la ubicación de esta reina
            tablero[i][col] = 0
    # si llegamos a este punto quiere decir que no se puede colocar ninguna reina en la columna
    return False


# función que ubica a las reinas o retorna null si no se pueden ubicar
def buscar_posiciones(n):
    # creamos la matriz, se llena sola de 0s
    tablero = np.zeros((n, n))

    # si no se pueden ubicar retornamos null
    if not ubicar_reinas(tablero, 0):
        return None
    # retornar tablero
    return tablero


tablero_prueba = buscar_posiciones(8)
# Imprimimos el tablero en caso de que exista solución, en caso contrario imprimimos None
print(tablero_prueba)
