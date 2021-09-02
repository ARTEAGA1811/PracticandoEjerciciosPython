def solucionar(numbers):
    registro = {}
    sinRepetir = list(set(numbers))

    for i in sinRepetir:
        sumatoria = 0
        for k in numbers:
            if(k!=i):
                sumatoria+=k
        registro[i] = sumatoria
    
    #ahora selecciono el correcto.
    aux = list(registro.values())
    claves = list(registro.keys())
    minimaSum = min(aux)
    listAux = []
    for i in claves:
        if(registro[i] == minimaSum):
            listAux.append(i)
    
    return(max(listAux))



def testear():
    casosPrueba = [
        [1,2,3,3,3,3,4,5,6,6],
        [0,7,1,-10,2,-4,-1,3,-2,10,-2,-6,-9,9,1,10,3,-2,0,9,6,-5,10,-10,-2,-5,-5,7,-6,-10,2,2,-5,-3,8,0,3,4,-2,-9,-8,-1,-5,-9,-3,-10,7,-3,-9,4,0,1,0,-9,-8,6,-5,1,-6,-1,0,9,-10,-9,-4,5,5,5,-1,-9,1,-7,-5,-4,0,7,-7,0,6,7,8,-2,0,-6,-6,-2,2,5,0,-4,6,-6,10,-8,-5,-5,7,0,7,-9],
        [2,-10,0,-8,4,-5,10,0,8,-9,4,-6,3,4,8,10,6,-5,2,-6,9,-10,4,-1,6,-1,7,10,-10,-3,-6,1,7,-1,9,-1,2,3,4,8,-3,-3,-5,5,-8,-1,9,8,8,0,-5,3,-6,-9,10,-8,-3,-4,-1,-8,-6,4,-10,1,7,-1,0,10,1,-1,-6,-2,-2,5,-1,-7,4,5,-5,6,-7,6,-2,-5,5,7,-4,8,0,8,-10,-7,-2,0,9,10,5,5,-8,9],
        [1,1,1,1,2,1],
        [1,1,1,1,1,1]
    ]

    salidas = [
        6,1,1,1,0
    ]

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = solucionar(casosPrueba[i])
            assert solution == salidas[i]
            print("respuesta correcta")
        except Exception as error:
            print(
                f"Error, test {casosPrueba[i]}, expected {salidas[i]}, calculated {solution}", error)

testear()