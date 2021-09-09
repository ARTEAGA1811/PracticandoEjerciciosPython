import math

def solucionar(a, b):
    mayor = a
    menor = b
    if(a < b):
        mayor = b
        menor = a
    # calculo el nivel de cada nodo.
    nivMayor = math.ceil(math.log(mayor+1, 2))
    nivMenor = math.ceil(math.log(menor+1, 2))
    # excepciones, casos rapidos.
    if(nivMenor == 1):
        return nivMayor-nivMenor

    # ahora debo calcular en que zona esta cada nodo.\
    numZonas = (2**(nivMenor-1))
    zonaMenor = menor - numZonas + 1
    aux = mayor
    for i in range(nivMayor-nivMenor):
        if aux % 2 == 0:
            aux /= 2
        else:
            aux -= 1
            aux /= 2
    zonaRelMayor = aux - numZonas+1

    # ahora calculo el numero de saltos
    totalSaltos = nivMayor-nivMenor
    # otra excepcion
    if(zonaMenor == zonaRelMayor):
        return totalSaltos
    #para facilitar las condicionales.
    zonaIzq = min(zonaMenor, zonaRelMayor)
    zonaDer = max(zonaMenor, zonaRelMayor)
    for k in range(int(math.log(numZonas, 2)-1)):
        numZonas /= 2
        if((zonaIzq <= numZonas and zonaDer > numZonas)):
            return totalSaltos + math.log(numZonas*2, 2)*2
        if(zonaIzq > numZonas and zonaDer > numZonas):
            zonaIzq -= (numZonas)
            zonaDer -= (numZonas)
    return totalSaltos+2


def testear():
    casosPrueba = [
        [1, 1],
        [1, 2],
        [2, 3],
        [10, 6],
        [19,15],
        [16,31],
        [6, 5],
        [14, 26],
        [12,17],
        [1000000000000000000,1000000010000000000]
    ]

    salidas = [
        0, 1, 2, 5, 7, 8, 4, 5, 7, 70
    ]

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = solucionar(casosPrueba[i][0], casosPrueba[i][1])
            assert solution == salidas[i]
            print("respuesta correcta")
        except Exception as error:
            print(
                f"Error, test {casosPrueba[i]}, expected {salidas[i]}, calculated {solution}", error)


testear()
