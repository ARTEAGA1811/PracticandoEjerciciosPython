class Vertice:
    #constructor
    def __init__(self, i):
        self.id = i
        self.visitado = False
        self.nivel = -1
        self.vecinos = []
    
    def agregarVecino(self, v):
        if v not in self.vecinos:
            self.vecinos.append(v)

class Grafica:
    #constructor
    def __init__(self):
        self.vertices = {}
    
    def agregarVertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = Vertice(v)
    
    def agregarArista(self, a, b):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregarVecino(b)
            self.vertices[b].agregarVecino(a)


def main():
        g = Grafica()

        miLista = [2,0,1,4,6,5,5]
        for i in miLista:
            g.agregarVertice(i)
        
        listaAristas = [2,0,0,6,6,3,0,5,5,6,0,1,6,4,1,4]
        for i in range(0,len(listaAristas)-1,2 ):
            g.agregarArista(listaAristas[i], listaAristas[i+1])


        for i in g.vertices:
            print(i, g.vertices[i].vecinos)


main()