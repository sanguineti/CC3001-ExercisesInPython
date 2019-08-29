class NodoLista:
    def __init__(self, val, sig=None):
        self.val = val
        self.sig = sig
    def __repr__(self):
        return repr(self.val)

class ListaCircular:
    def __init__(self):
        self.primero = None
        self.size = 0

    def largo(self):
        return self.size
    
    def obtener(self, i):
        if self.size==0:
            return -1
        buscador = self.primero
        for x in range(i):
            buscador = buscador.sig
        return buscador.val
    
    def existe(self, num):
        buscador = self.primero
        for x in range(self.size):
            if int(buscador.val) == num:
                return x
            buscador = buscador.sig
        return -1      
    def eliminar(self, i):
        if self.size==0:
            return None
        buscador = self.primero
        if (i == 1):
            for x in range(1, self.size):
                buscador = buscador.sig
        else:
            for x in range(1, i - 1):
                buscador = buscador.sig
        print("Eliminado: ", buscador.sig.val)
        buscador.sig = buscador.sig.sig
        self.size -= 1
        return buscador.sig

    def agregar(self, v):
        if self.size == 0:
            self.primero = NodoLista(v)
            self.primero.sig = self.primero #Lista Circular
            self.size += 1
            return
    
        nodo_nuevo = NodoLista(v, self.primero)
        ultimo_antiguo = self.primero
        for x in range(1,self.size):
            ultimo_antiguo = ultimo_antiguo.sig
        ultimo_antiguo.sig = nodo_nuevo
        self.size += 1


lista = ListaCircular()
lista.agregar(5)
lista.agregar(3)
lista.agregar(90)
lista.agregar(182937129837)
print(lista.obtener(1))