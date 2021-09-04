#hasta ahora este es el mejor. tiempo 10^7 aprox 16 segundos
def reiniciarContadorVivas(regVivas):
    listaClaves = list(regVivas.keys()) #['1,2', '3,4', '4,5' ,....]
    for i in listaClaves:
        regVivas[i] = 0

def eliminarVivas(regVivas: dict):
    listaClaves = list(regVivas.keys()) #['1,2', '3,4', '4,5' ,....]
    for i in listaClaves:
        if(regVivas[i] != 2 and regVivas[i] != 3):
            regVivas.pop(i,-1)

def agregarNuevasVivas(regVivas: dict, regMuertas: dict):
    listaClaves = list(regMuertas.keys()) #['1,2', '3,4', '4,5' ,....]
    for i in listaClaves:
        if(regMuertas[i] == 3):
            regVivas[i] = 0 #agrego a la lista de vivas.

def calcularVivas_Muertas(regVivas: dict, regMuertas: dict, numFil, numCol):
    listaClaves = list(regVivas.keys()) #['1,2', '3,4', '4,5' ,....]
    for i in listaClaves:
        p = i.split(',')
        a = [int(p[0]), int(p[1])]
        ar = a[0] -1
        ab = a[0] + 1
        izq = a[1] -1
        der = a[1] +1
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
        #primero se revisa que el vecino no este vivo
        vecAr= str(ar)+','+str(a[1])
        vecAb= str(ab)+','+str(a[1])
        vecIzq = str(a[0])+','+str(izq)
        vecDer = str(a[0])+','+str(der)
        vecSupIz = str(ar)+','+str(izq)
        vecSupDer = str(ar)+','+str(der)
        vecInfIzq = str(ab)+','+str(izq)
        vecInfDer = str(ab)+','+str(der)
        aux = [vecAr,vecAb,vecIzq, vecDer,vecSupIz,vecSupDer, vecInfIzq,vecInfDer]
        for bucle in aux:
            #si el vecino esta muerto lo agrego a regMuertas
            if bucle not in regVivas:
                #si no esta aun: lo agrego, si ya esta: le aumento uno
                if bucle not in regMuertas:
                    regMuertas[bucle] = 1
                else:
                    regMuertas[bucle] = regMuertas[bucle]+1
            else:
                #si el vecino es un viva, agrego uno a mi.
                regVivas[i] = regVivas[i] +1

def generarMatrizFinal(regVivas: dict, numFil, numCol):
    nuevaMatriz = []
    for i in range(numFil):
        aux = ''
        for k in range(numCol):
            if(str(i)+','+str(k) in regVivas):
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
                regVivas[str(i)+','+str(k)] = 0
    #empiezo con las iteraciones
    for iter in range(c):
        #en cada iteracion, las regMuertas empiezan de 0, y reinicio los contadores de las vivas
        regMuertas = {}
        reiniciarContadorVivas(regVivas)
        calcularVivas_Muertas(regVivas, regMuertas, numFil, numCol)
        #ahora ya tengo las respectivas vivas y muertas que importan.
        #elimino las vivas que tengan vecinosvivos <2 o >3
        eliminarVivas(regVivas)
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

