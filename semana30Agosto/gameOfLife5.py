
def eliminarYReiniciarVivas(regVivas: dict):
    #en cada iteracion analizo el diccionario que guarda las vivas, si no cumplen con su condicion, las elimino
    #del diccionario, en caso que cumplan, reinicio sus valores a 0.
    listaClaves = list(regVivas.keys()) #[(1,2), (3,4),(4,5) ,....]
    for i in listaClaves:
        if(regVivas[i] != 2 and regVivas[i] != 3):
            regVivas.pop(i,-1)
        else:
            regVivas[i] = 0

def agregarNuevasVivas(regVivas: dict, regMuertas: dict):
    #Se analizan los vecinos muertos, en caso que tengan 3 vecinas vivas, los añado al diccionario de las vivas.
    listaClaves = list(regMuertas.keys()) #[(1,2), (3,4),(4,5) ,....]
    for i in listaClaves:
        if(regMuertas[i] == 3):
            regVivas[i] = 0 #agrego a la lista de vivas.

def calcularVivas_Muertas(regVivas: dict, regMuertas: dict, numFil, numCol):

    listaClaves = list(regVivas.keys()) #[(1,2), (3,4),(4,5) ,....]
    #recorro las vivas.
    for i in listaClaves:
        ar = i[0] -1
        ab = i[0] + 1
        izq = i[1] -1
        der = i[1] +1
        #reviso los limites.
        if(ar<0):
            ar = numFil-1
        if(ab>numFil-1):
            ab = 0
        if(izq<0):
            izq = numCol-1
        if(der>numCol-1):
            der = 0
        #se agregan las celulas muertas.

        #aqui se guardan los 8 vecinos de la celula viva.
        aux = [(ar,i[1]), (ab,i[1]), (i[0],izq),(i[0],der),(ar,izq),(ar,der),(ab,izq), (ab,der)]
        for bucle in aux:
            #si el vecino esta muerto lo agrego a regMuertas
            if bucle not in regVivas:
                #si no esta aun: lo agrego, si ya esta: le aumento uno
                if bucle not in regMuertas:
                    regMuertas[bucle] = 1
                else:
                    regMuertas[bucle] = regMuertas[bucle]+1
            else:
                #si el vecino es una viva, agrego uno a mi.
                regVivas[i] = regVivas[i] +1

def generarMatrizFinal(regVivas: dict, numFil, numCol):
    #al final, genero la matriz analizando las celulas vivas que me quedaron.
    nuevaMatriz = []
    for i in range(numFil):
        aux = ''
        for k in range(numCol):
            if((i,k) in regVivas):
                aux+='*'
            else:
                aux+='-'
        nuevaMatriz.append(aux)
    return nuevaMatriz

def solucionar(arr,c):
    numFil = len(arr)
    numCol = len(arr[0])
    regVivas = {}
    #recorro matriz.
    for i in range(numFil):
        for k in range(numCol):
            #lleno las vivas.
            if(arr[i][k] == '*'):
                regVivas[(i,k)] = 0
    #empiezo con las iteraciones
    for iter in range(c):
        #en cada iteracion, las regMuertas empiezan de 0, y reinicio los contadores de las vivas
        regMuertas = {}
        calcularVivas_Muertas(regVivas, regMuertas, numFil, numCol)
        #ahora ya tengo las respectivas vivas y muertas que importan.
        #elimino las vivas que tengan vecinosvivos <2 o >3
        eliminarYReiniciarVivas(regVivas)
        #ahora agrego al registro de las vivas: las celulas muertas que tengan 3 vecinos vivos.
        agregarNuevasVivas(regVivas,regMuertas)
    #ahora lleno la matriz final.
    return generarMatrizFinal(regVivas,numFil,numCol)







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
            ],1
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

