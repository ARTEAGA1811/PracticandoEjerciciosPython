#https://csacademy.com/ieeextreme-practice/task/e610aba28810ebcf2d3998692269b5a0/statement/


def calcularMejorRuta(nivel, posY, posX, registros, r,c, arr):
    if(posY == r and posX == c):
        return 0
    elif((str(posY)+str(posX)) in registros):
        return registros[str(posY)+str(posX)] + arr[posY][posX]
    elif(posY == r):
        aux = calcularMejorRuta(nivel+1, posY, posX+1, registros, r, c, arr)
        registros[str(posY)+str(posX)] = aux
        return aux + arr[posY][posX]

    elif(posX == c):
        aux = calcularMejorRuta(nivel+1, posY+1, posX, registros, r, c, arr)
        registros[str(posY)+str(posX)] = aux
        return aux + arr[posY][posX]
    else:
        aux = max(calcularMejorRuta(nivel+1, posY+1, posX, registros, r,c, arr) , calcularMejorRuta(nivel+1, posY, posX+1, registros, r,c, arr))
        registros[str(posY)+str(posX)] = aux
        return  aux + arr[posY][posX]






def solucionar(a, matris):
    registros = {}
    mejorRuta = calcularMejorRuta(0, 0, 0, registros, a[0]-1, a[1]-1, matris)
    print('mejor ruta', mejorRuta)
    if(mejorRuta>= 1):
        return 1
    return 1-mejorRuta



def testear():
    casosPrueba = [
        [
            [2,2],
            [
                [0,-2],
                [2,0]
            ]
        ],
        [
            [3,3],
            [
                [0,1,2],
                [-2,-9,-4],
                [-8,5,0]
            ]
        ]

    ]

    salidas = [
        1,2
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