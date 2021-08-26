
def solucionar2(string):
    #test = int(input())
    #for i in range(test):
    aux = string[0]
    aux = aux.split()
    sum = int(aux[0])
    numEntradas = int(aux[1])
    auxLista = string[1]
    auxLista = auxLista.split()
    miLista = list()
    for con in auxLista:
        miLista.append(int(con))
    #Empiezo a analizar
    if(numEntradas == 0 or numEntradas == 1):
        return('!OK')
        #continue
    else:
        for salto in range(1, len(miLista)):
            for buc in range(0, len(miLista)-salto, 1):
                if((miLista[buc] + miLista[buc+salto]) == sum):
                    if(miLista[buc]<miLista[buc+salto]):
                        return(str(miLista[buc])+' '+str(miLista[buc+salto]))
                    else:
                        return(str(miLista[buc+salto])+' '+str(miLista[buc])) 
  
        return('!OK')



def solucionar(string):
    aux = string[0]
    aux = aux.split()
    sum = int(aux[0])
    numEntradas = int(aux[1])
    auxLista = string[1]
    auxLista = auxLista.split()
    miLista = list()
    for con in auxLista:
        miLista.append(int(con))
    #Empiezo a analizar
    arrSol = []
    loquefalta = set()
    for i in miLista:
        if(i in loquefalta):
            arrSol.append(i)
            arrSol.append(sum-i)
            arrSol.sort()
            return(str(arrSol[0])+' '+ str(arrSol[1]))
        else:
            loquefalta.add(sum-i)
    return('!OK')

def testear():
    casosPrueba = [
        ['8 4', '1 2 4 4'], ['8 4', '1 2 7 9'], ['8 4', '1 2 8 9'], ['8 4', '4 5 3 4'], ['8 4', '4 1 1 8'], 
        ['8 4', '-1 1 9 8'], ['12 4', '5 0 8 9'], ['13 4', '10 0 6 1'], ['17 3', '2 9 4'], 
        ['0 8', '2 7 6 5 3 9 8 0'], ['4 0', ''], ['4 0', ''], ['7 7', '8 10 9 7 4 6 2'], ['13 3', '6 7 1'], 
        ['2 7', '10 7 5 1 0 3 9'], ['0 1', '-1']
        ]

    casosPruebae =  [['-250 7', '9 1 2 3 4 5 -14']]
       
    salidas = ['4 4', '1 7', '!OK', '3 5', '!OK', '-1 9', '!OK', '!OK', '!OK', '!OK', '!OK', '!OK', '!OK', '6 7', '!OK', '!OK']
    salidase = ['-400 2']     

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = solucionar(casosPrueba[i])
            assert solution == salidas[i]
            print("ta bien")
        except Exception as error:
            print(f"Error, test {casosPrueba[i]}, expected {salidas[i]}, calculated {solution}", error)


def entregar():
    numCasos = int(input())
    for i in range(numCasos):
        miLista = list()
        e1 = input()
        e2 = input()
        miLista.append(e1)
        miLista.append(e2)

        print(solucionar(miLista))

#entregar()
testear() 
