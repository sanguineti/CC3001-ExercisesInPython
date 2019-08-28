class NodoLista:
    def __init__(self, val=None, sig=None):
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
            if buscador.val == num:
                return x + 1
            buscador = buscador.sig
        return -1      
        