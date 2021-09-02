
def duplicateZeros(arr: list):
    tam = len(arr)
    saltarUno = False
    for i in range(tam):
        if(saltarUno == False): 
            if(arr[i] == 0):
                saltarUno = True
                auxUno = 0
                auxDos = 0
                for k in range(i+1, tam):
                    auxDos = auxUno
                    if k < tam-1:
                        auxUno = arr[k]
                    arr[k] = auxDos
        else:
            saltarUno = False
        
    print(arr)


duplicateZeros([1, 0, 2, 3,0,4,5,0])
