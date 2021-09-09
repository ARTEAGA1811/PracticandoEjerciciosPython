import math
class Nodo:
    def __init__(self,dato) -> None:
        self.dato = dato
        self.izq = None
        self.der = None

class Arbol:
    def __init__(self, dato) -> None:
        self.raiz = Nodo(dato)

    def agregar(self, dato, nivel, nivelMax , miNodo):
        #caso recursivo
        if nivel != nivelMax:
            #agrego a la izq.
            miNodo.izq = Nodo(dato*2)
            #voy a la izq.
            self.agregar(dato*2, nivel+1, nivelMax, miNodo.izq)
            #agrego derecha.
            miNodo.der = Nodo(dato*2+1)
            self.agregar(dato*2+1, nivel+1, nivelMax, miNodo.der)

    def imprimirArbol(self, miNodo: Nodo):
        if miNodo != None:
            print(miNodo.dato)
            self.imprimirArbol(miNodo.izq)
            self.imprimirArbol(miNodo.der)
        else:
            print("regreso")


def main():
    e = 10000000
    miArbol = Arbol(1)
    nivelMax = math.ceil(math.log(e+1,2))
    miArbol.agregar(1, 1, nivelMax, miArbol.raiz)
    #miArbol.imprimirArbol(miArbol.raiz)


main()

