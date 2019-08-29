class NodoLista:
    def __init__(self, v, s=None):
        self.val = v
        self.sig = s

    def __repr__(self):
        return repr(self.val)


class ListaCircular:
    def __init__(self):
        self.primero = None
        self.size = 0

    # Retorna la cantidad de elementos en la lista
    def largo(self):
        return self.size

    # Retorna el i-ésimo elemento de la lista, contando desde 1
    def obtener(self, i):
        if self.size == 0:
            return -1
        buscador = self.primero
        for x in range(1, i):
            buscador = buscador.sig
        return buscador.val

    # Retorna el índice del elemento si existiese, de lo contario retorna -1
    def existe(self, num):
        buscador = self.primero
        for x in range(self.size):
            if int(buscador.val) == num:
                return x
            buscador = buscador.sig
        return -1

    # Elimina el i-ésimo eleento y retorna la referencia al siguiente nodo del eliminado
    def eliminar(self, i):
        if self.size == 0:
            return None
        # Avanzar hasta quedar en la posición anterior al elemento a eliminar
        buscador = self.primero
        if (i == 1):  # Primer elemento es un caso especial
            # Recorremos hasta el último nodo para que quede en el nodo anterior al primero
            for x in range(1, self.size):
                buscador = buscador.sig
        else:
            # Caso general
            for x in range(1, i - 1):
                buscador = buscador.sig
        # Aquí estamos en el nodo anterior al que queremos eliminar, ahora lo eliminamos.
        print("Eliminado: ", buscador.sig.val)
        buscador.sig = buscador.sig.sig # Cambio la referencia
        self.size -= 1
        return buscador.sig # Retornar el siguiente al eliminado

    def agregar(self, v):
        if self.size == 0: # No elementos
            self.primero = NodoLista(v)
            self.primero.sig = self.primero  # Lista Circular
            self.size += 1
            return
        # Si existen elementos
        nodo_nuevo = NodoLista(v, self.primero) #Como lo inserto al final, apunta al primero
        ultimo_antiguo = self.primero
        for x in range(1, self.size):
            ultimo_antiguo = ultimo_antiguo.sig
        ultimo_antiguo.sig = nodo_nuevo # Ahora apunta al nuevo
        self.size += 1
