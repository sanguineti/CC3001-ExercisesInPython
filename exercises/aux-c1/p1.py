class Nodo:
    def __init__(self, val, sig):
        self.valor = val
        self.sgte = sig


def elementosDistintos(n1, n2):
    ans = 0
    while(n1 != None or n2 != None):
        if(n1 == None):
            ans += 1
            n2 = n2.sgte

        elif(n2 == None):
            ans += 1
            n1 = n1.sgte

        elif(n1.valor < n2.valor):
            ans += 1
            n1 = n1.sgte

        elif(n1.valor > n2.valor):
            ans += 1
            n2 = n2.sgte

        else:
            n1 = n1.sgte
            n2 = n2.sgte

    return ans

if __name__ == "__main__":
    a = Nodo(12, Nodo(22, Nodo(45, Nodo(67, Nodo(81, Nodo(99, None))))))
    b = Nodo(8, Nodo(17, Nodo(22, Nodo(60, Nodo(81, None)))))
    c = elementosDistintos(a,b)
    print(c)
