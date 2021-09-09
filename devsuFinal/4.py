def encontrarMaxMom(damage, victories, nivelAct, maxNivel, ind, tam):
    #casos base
    if nivelAct == maxNivel or ind == tam:
        return damage[ind], victories[ind]
    #casos recursivos
    listaAux = []
    for k in range(ind+1, tam+1):
        gg = encontrarMaxMom(damage, victories, nivelAct+1, maxNivel, ind+1, tam)
        sumatoria = gg[0]
        numVic =  gg[1]
        listaAux.append((sumatoria+damage[ind])*min(victories[ind],numVic))
    return max(listaAux)

def solucionar(damage, victories, c):
    tam = len(damage)
    guardar = []
    for bucle in range(c):
        for i in range(tam):
            valor = encontrarMaxMom(damage, victories, 1, bucle+1, i, tam-1)
            guardar.append(valor)
    
    return max(guardar)


def testear():
    casosPrueba = [
        [
            [1,2,3,4],
            [4,3,2,1],
            3

        ]
    ]

    salidas = [
        12
    ]

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = solucionar(casosPrueba[i][0], casosPrueba[i][1], casosPrueba[i][2])
            assert solution == salidas[i]
            print("respuesta correcta")
        except Exception as error:
            print(
                f"Error, test {casosPrueba[i]}, expected {salidas[i]}, calculated {solution}", error)

testear()