class Vertice:  
    def __init__(self, id):       
        self.id = id
        self.vecinos = []
    
    def agregarVecino(self,vec):
        self.vecinos.append(vec)
    
    def numVecinos(self):
        sumatoria = 0
        for i in self.vecinos:
            sumatoria+=i
        return sumatoria
    
    def esHoja(self):
        if (len(self.vecinos) <=1):
            return True
        else:
            return False
    
    def borrarVerticeDelVecino(self, vec):
        if vec in self.vecinos:
            self.vecinos.remove(vec)
    
    def __str__(self) -> str:
        mensaje = str('(id:'+str(self.id)+' vecinos: '+str(self.vecinos)+')')
        return mensaje



t = int(input())
#t = 1
for numCasos in range(t):
    ingreso = input()
    #ingreso = '4 5'
    ingreso = ingreso.split()
    ver = int(ingreso[0])
    aris = int(ingreso[1])

    ingreso = input()
    #ingreso = '0 1 0 2 1 2 2 3 0 3'
    ingreso = ingreso.split()
    listaAristas = list()
    for i in ingreso:
        listaAristas.append(int(i))

    listaCompleta = {}
    for x in range(0, len(listaAristas)-1, 2):
        if( listaAristas[x] not in listaCompleta):
            listaCompleta[listaAristas[x]] = Vertice(listaAristas[x])
            #ahora se agregan los vecinos
            listaCompleta[listaAristas[x]].agregarVecino(listaAristas[x+1])
        else:
            #aqui ya existe
            listaCompleta[listaAristas[x]].agregarVecino(listaAristas[x+1])
    
    for y in range(1, len(listaAristas), 2):
        if(listaAristas[y] not in listaCompleta):
            listaCompleta[listaAristas[y]] = Vertice(listaAristas[y])
            #ahora se agregan los vecinos
            listaCompleta[listaAristas[y]].agregarVecino(listaAristas[y-1])
        else:
            #aqui ya existe
            listaCompleta[listaAristas[y]].agregarVecino(listaAristas[y-1])

    '''for bucle in listaCompleta:
        print(bucle, listaCompleta[bucle]) '''


    #HASTA AQUITODO ESTA BIEN

    continuar = True
    while(continuar):
        continuar = False
        verticeAEliminar = 0
        for bucle in listaCompleta:
            if(listaCompleta[bucle].esHoja() and len(listaCompleta) != 0):
                continuar = True
                verticeAEliminar = int(listaCompleta[bucle].id)
                break
            
            
        
        if(continuar == False):
            if(len(listaCompleta) == 0):
                print(0)
            else:
                print(1)
            
        else:
            #Aqui significa que toca seguir borrando
            #primero elimino el vertice
            listaCompleta.pop(verticeAEliminar)

            #Ahora lo elimino donde conste como vecino
            for bucle in listaCompleta:
                listaCompleta[bucle].borrarVerticeDelVecino(verticeAEliminar)

            


