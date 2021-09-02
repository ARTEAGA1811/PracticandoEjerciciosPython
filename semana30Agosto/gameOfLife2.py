def cambiarMatriz(regCambios, arr):
    listaClaves = list(regCambios.keys())
    #print(listaClaves)
    for i in range(len(listaClaves)):
        a = int(listaClaves[i][0])
        b = int(listaClaves[i][1])
        valor = str(regCambios[listaClaves[i]])
        arr[a] =  arr[a][:b] + valor + arr[a][b+1:] 

def getNumVVivos(arr, i, k):
    contador = 0
    tamFil = len(arr)
    tamCol = len(arr[0])

    arriba = i-1
    abajo = i+1
    izq = k-1
    der = k+1
    #reviso los limites.
    if(arriba<0):
        arriba = tamFil-1
    if(abajo>tamFil-1):
        abajo = 0
    if(izq<0):
        izq = -1
    if(der>tamCol-1):
        der = 0
    
    if(arr[arriba][k] == '*'): #arriba
        contador+=1
    if(arr[abajo][k] == '*'): #abajo
        contador+=1
    if(arr[i][izq] == '*'): #izq
        contador+=1
    if(arr[i][der] == '*'): #derecha
        contador+=1
    if(arr[arriba][izq] == '*'): #diagonal Sup izq
        contador+=1
    if(arr[arriba][der] == '*'): #diagonal Sup der
        contador+=1
    if(arr[abajo][izq] == '*'): #diagonal Inf izq
        contador+=1
    if(arr[abajo][der] == '*'): #diagonal Inf der
        contador+=1
    return contador

def solucionar(arr, c):
    fil = len(arr)
    col = len(arr[0])
    
    for bucle in range(c):
        regCambios = {}
        for i in range(fil):
            for k in range(col):
                numVVivos = getNumVVivos(arr, i, k)
                if(arr[i][k] == '*'):
                    if( numVVivos== 2 or numVVivos == 3):
                        continue
                    else:
                        regCambios[str(i)+str(k)] = '-'
                else: #que son -
                    if(numVVivos == 3):
                        regCambios[str(i)+str(k)] = '*'
        cambiarMatriz(regCambios, arr)
    
    return arr

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
            ],1000000
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
