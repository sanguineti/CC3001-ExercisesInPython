from P1 import ListaCircular


def josephus(clista, k):
    nodo = clista.primero
    while clista.largo() > 1:
        # El siguiente al eliminado (recordar que cuenta desde 1)
        nodo = clista.eliminar(k+1)
        clista.primero = nodo
    return nodo.val


# Esta función genera una lista circular con cada elemento con el entero correspondiente a su posición en el primer conteo
def generar_lista(cant):
    lista = ListaCircular()
    for i in range(1, cant + 1):
        lista.agregar(i)
    return lista

# Main, desde aquí corre el programa
if __name__ == "__main__":
    lista = ListaCircular()
    for k in range(1, 11): # De uno a diez
        lista = generar_lista(6)
        print("Último niño en la lista para k = ", k, ": ", josephus(lista, k))