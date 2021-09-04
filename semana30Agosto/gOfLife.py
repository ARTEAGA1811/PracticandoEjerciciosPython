#no sirve, tiempo excedido.
def genMNum(arr, numFil, numCol):
    arrNum = []
    for i in range(numFil):
        aux = []
        for k in range(numCol):
            # creo el array..
            if(arr[i][k] == '*'):
                aux.append(1)
            else:
                aux.append(0)
        arrNum.append(aux)
    return arrNum


def cambiarMatriz(arrNum, regCambios):
    for i in regCambios:
        if arrNum[i[0]][i[1]] == 0:
            arrNum[i[0]][i[1]] = 1
        else:
            arrNum[i[0]][i[1]] = 0


def regresarMatriz(arrNum, numFil, numCol):
    arrDef = []
    for i in range(numFil):
        aux = ''
        for k in range(numCol):
            # creo el array..
            if(arrNum[i][k] == 0):
                aux += '-'
            else:
                aux += '*'
        arrDef.append(aux)
    return arrDef


def solucionar(arr, c):
    numFil = len(arr)
    numCol = len(arr[0])
    arrNum = genMNum(arr, numFil, numCol)
    regCambios = []
    for iter in range(c):
        regCambios = []
        for i in range(numFil):
            for k in range(numCol):
                ar = i-1
                ab = i+1
                izq = k-1
                der = k+1
                # se corrigen los que tengan limites
                if(ar < 0):
                    ar = numFil-1
                if(ab > numFil-1):
                    ab = 0
                if(izq < 0):
                    izq = numCol-1
                if(der > numCol-1):
                    der = 0

                suma = arrNum[ar][k] + arrNum[ab][k] + arrNum[i][izq] + arrNum[i][der] + arrNum[ar][izq] + arrNum[ar][der] + arrNum[ab][izq] + arrNum[ab][der]
                if(arrNum[i][k] == 0):
                    if suma == 3:
                        aux = [i, k]
                        regCambios.append(aux)
                else:
                    if suma != 2 and suma != 3:
                        aux = [i, k]
                        regCambios.append(aux)

        # aqui se cambia la matriz con los cambios encontrados
        cambiarMatriz(arrNum, regCambios)
    return regresarMatriz(arrNum, numFil, numCol)


def testear():
    casosPrueba = [
        [
            [
                '------',
                '------',
                '------',
                '-***--'
            ], 3
        ],
        [
            [
                '------',
                '--*---',
                '---*--',
                '-***--',
                '------'
            ], 1234
        ],
        [
            [
                '---------',
                '---------',
                '---------',
                '--*****--',
                '---------',
                '---------',
                '---------'
            ], 5
        ],
        [
            [
                '-----*',
                '--*---',
                '*-----',
                '-***-*'
            ], 10000000
        ]

    ]

    salidas = [
        [
            '--*---',
            '------',
            '--*---',
            '--*---'
        ],
        [
            '-----*',
            '---*-*',
            '----**',
            '------',
            '------'
        ],
        [
            '----*----',
            '---***---',
            '--*-*-*--',
            '-***-***-',
            '--*-*-*--',
            '---***---',
            '----*----'
        ],
        [
            '**-**-',
            '------',
            '*--*--',
            '-**-**'
        ]
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
