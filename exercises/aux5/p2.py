from P1 import ListaCircular

def josephus(clista, k):
    nodo = clista.primero
    while clista.largo() > 1:
        nodo = clista.eliminar(1+k) #El siguiente al eliminado
    return nodo.val