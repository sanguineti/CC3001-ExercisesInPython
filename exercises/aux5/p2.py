from P1 import ListaCircular


def josephus(clista, k):
    nodo = clista.primero
    while clista.largo() > 1:
        # El siguiente al eliminado (recordar que cuenta desde 1)
        nodo = clista.eliminar(1+k)
    return nodo.val


# Esta función genera una lista circular con cada elemento con el entero correspondiente a su posición en el primer conteo
def generar_lista(cant):
    lista = ListaCircular()
    for i in range(1, cant + 1):
        lista.agregar(i)
    return lista
