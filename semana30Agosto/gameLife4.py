#inconcluso.
def genMNum (arr, numFil, numCol):
    arrNum = []
    regVivos = []
    for i in range(numFil):
        aux = []
        for k in range(numCol):
            #creo el array..
            if(arr[i][k] == '*'):
                aux.append(1)
                a = [i,k]
                regVivos.append(a)
            else:
                aux.append(0)
        arrNum.append(aux)
    return arrNum, regVivos
        
def calcularVivas_Muertas(arrNum, regVivas:list, numFil, numCol):
    #recorro vivas
    vecMuert = set()
    regCambios = []
    for i in regVivas:
        #se definen los vecinos.
        ar = i[0]-1
        ab = i[0]+1
        izq = i[1]-1
        der = i[1]+1
        #se corrigen los que tengan limites
        if(ar<0):
            ar = numFil-1
        if(ab>numFil-1):
            ab = 0
        if(izq<0):
            izq = numCol-1
        if(der>numCol-1):
            der = 0
        #guardo vecinos.
        aux = [[ar, i[1]], [ab, i[1]], [i[0], izq], [i[0], der], [ar, izq], [ar, der], [ab, izq], [ab,der]]
        for bucle in aux:
            if bucle not in regVivas:
                #aqui significa que el vecino es una celula muerta.
                vecMuert.add(bucle)
        #ahora analizo esta celula viva.
        suma = arrNum[ar][i[1]] + arrNum[ab][i[1]] + arrNum[i[0]][izq] + arrNum[i[0]][der] + arrNum[ar][izq] + arrNum[ar][der] + arrNum[ab][izq] + arrNum[ab][der]
        if(suma != 2 and suma != 3):
            regVivas.remove(i) #elimino la celula viva si no cumple.
    
    #ahora tengo que analizar los vecinos muertos.
    #en caso que un vecino cumpla se le agrega a la lista de las vivas,
    for it in vecMuert:
         pass
        




def solucionar(arr,c):
    numFil = len(arr)
    numCol = len(arr[0])
    regVivas = []
    arrNum, regVivas = genMNum(arr, numFil, numCol)
    #print(arrNum)
    #print(regVivas)
    #empiezo con las iteraciones
    for iter in range(c):
        #en cada iteracion, las regMuertas empiezan de 0, y reinicio los contadores de las vivas
        regMuertas = {}
        #reiniciarContadorVivas(regVivas)
        calcularVivas_Muertas(arrNum, regVivas)
    #     #ahora ya tengo las respectivas vivas y muertas que importan.
    #     #elimino las vivas que tengan vecinosvivos <2 o >3
    #     eliminarVivas(regVivas)
    #     #ahora agrego al registro de las vivas: las celulas muertas que tengan 3 vecinos vivos.
    #     agregarNuevasVivas(regVivas,regMuertas)
    # #ahora lleno la matriz final.
    # return generarMatrizFinal(regVivas,numFil,numCol)


def testear():
    casosPrueba = [
        [   
            [
                '------',
                '------',
                '------',
                '-***--'
            ],3
        ],
        [
            [
                '------',
                '--*---',
                '---*--',
                '-***--',
                '------'
            ],1234
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
            ],5
        ],
        [
            [
                '-----*',
                '--*---',
                '*-----',
                '-***-*'
            ],10000000
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
            solution = solucionar(casosPrueba[i][0],casosPrueba[i][1])
            assert solution == salidas[i]
            print("respuesta correcta")
        except Exception as error:
            print(
                f"Error, test {casosPrueba[i]}, expected {salidas[i]}, calculated {solution}", error)

testear()