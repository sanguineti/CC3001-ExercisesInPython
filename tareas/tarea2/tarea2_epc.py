import numpy as np

def recibir_input():
    a = input()
    return np.fromstring(a, dtype=int, sep=' ')


def move(s, arreglo, fuente, aux, destino):
    if arreglo.size == 1:
        imprimir_movimiento(fuente, destino, arreglo[s-1])
        return 
    move(s-1, arreglo[:-1], fuente, destino, aux)
    imprimir_movimiento(fuente, destino, arreglo[s-1])
    move(s-1, arreglo[:-1], aux, fuente, destino)


def imprimir_movimiento(fuente, destino, veces):
    for i in range(veces):
        print('{}{}'.format(fuente, destino), end="")

        
def main():
    a = recibir_input()
    if a.size == 0:
        return
    move(len(a), a, 'A', 'B', 'C')


main()
