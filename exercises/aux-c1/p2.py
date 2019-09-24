class ArbolBinario:
    def __init__(self, val, izq=None, der=None):
        self.info = val
        self.izq = izq
        self.der = der

def pesos(raiz):
	# caso base si la raiz es nula tiene peso 0
	if(raiz == None): 
		return 0
	
	pesoIzq = pesos(raiz.izq)   # calculamos el peso a la izquierda
	pesoDer = pesos(raiz.der)   # lo mismo a la derecha

	if(pesoIzq == pesoDer):
		print(raiz.info)

	# se retorna el peso de los hijos mas el peso que aporta la raiz
	return pesoIzq + pesoDer + 1

if __name__ == "__main__":


    a = ArbolBinario(5,
                        ArbolBinario(3,
                                        ArbolBinario(2),
                                        ArbolBinario(4)),
                        ArbolBinario(7,
                                        ArbolBinario(6),
                                        ArbolBinario(8,
                                                    None,
                                                    ArbolBinario(9))))
    b = ArbolBinario(5,
                            ArbolBinario(3,
                                        ArbolBinario(2),
                                        ArbolBinario(16)),
                            ArbolBinario(8,
                                        ArbolBinario(7),
                                        ArbolBinario(9)))
    print("el peso del arbol a es:", pesos(a))
    print()
    print("el peso del arbol b es:", pesos(b))
