def generarNUevaMatriz(B):
    A = []
    tamFilaB = len(B)-1
    aux = B[tamFilaB].copy() #agrego la ultima fila
    aux = [B[tamFilaB][-1]] + aux #agrego la ultima columna de la ultima fila, al inicio
    aux.append(B[tamFilaB][0]) #agrego la primera columna de la ultima fila , al final
    #agrego a A
    A.append(aux)
    #ahora voy recorriendo cada fila de B y solo le agrego a los extremos
    for i in range (tamFilaB+1):
        auxDos = B[i].copy()
        auxDos = [B[i][-1]] + auxDos #agrego al inicio
        auxDos.append(B[i][0]) #agrego al final
        #agrego en A
        A.append(auxDos)
    #agrego la fila del inicio al final.
    auxTres =  B[0].copy()
    auxTres = [B[0][-1]] + auxTres
    auxTres.append(B[0][0])
    A.append(auxTres)

    return A


def cambiarMatriz(regCambios: dict, A):
    for clave in regCambios.keys():
        A[int(clave[0])][int(clave[1])] = regCambios[clave]



def getNumVecinosVivos(A,i,k):
    contador = 0
    #arriba:
    if(A[i-1][k] == '*'): #arriba
        contador+=1
    if(A[i+1][k] == '*'): #abajo
        contador+=1
    if(A[i][k-1] == '*'): #izq
        contador+=1
    if(A[i][k+1] == '*'): #derecha
        contador+=1
    if(A[i-1][k-1] == '*'): #diagonal Sup izq
        contador+=1
    if(A[i-1][k+1] == '*'): #diagonal Sup der
        contador+=1
    if(A[i+1][k-1] == '*'): #diagonal Inf izq
        contador+=1
    if(A[i+1][k+1] == '*'): #diagonal Inf der
        contador+=1
    return contador


def solucionarUno(arr, c): 
    fil = len(arr)
    col = len(arr[0])
    A = generarNUevaMatriz(arr)
    for bucle in range(c):
        regCambios = {}
        for i in range(1,len(A)-1):
            for k in range(1, len(A[0])-1):
                numVVivos = getNumVecinosVivos(A,i,k)
                if(A[i][k] == '*'):
                    if( numVVivos== 2 or numVVivos == 3):
                        continue
                    else:
                        regCambios[str(i)+str(k)] = '-'
                else: #que son -
                    if(numVVivos == 3):
                        regCambios[str(i)+str(k)] = '*'
        
        #se hace el cambio
        cambiarMatriz(regCambios, A)
    
    print(A)
    return A[1:-2][1:-2]






def testear():
    casosPrueba = [
        [
            ['------'],
            ['------'],
            ['------'],
            ['-***--']
        ]

    ]

    salidas = [
        [
            ['--*---'],
            ['------'],
            ['--*---'],
            ['--*---']
        ]
    ]

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = solucionarUno(casosPrueba[i], 3)
            assert solution == salidas[i]
            print("respuesta correcta")
        except Exception as error:
            print(
                f"Error, test {casosPrueba[i]}, expected {salidas[i]}, calculated {solution}", error)

testear()
