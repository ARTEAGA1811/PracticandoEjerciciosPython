def generarMin(arr, numSalto, saltosMax, libroCostos: dict):  
    #casos base
    if(numSalto in libroCostos):
        return(libroCostos[numSalto]+arr[numSalto-1])
    elif(numSalto == saltosMax):
        #libroCostos[numSalto] = arr[numSalto-1]
        return(0)
    elif(numSalto == saltosMax-1): #caso recursivo 1.
        costoMinino = generarMin(arr, numSalto+1, saltosMax, libroCostos)
        libroCostos[numSalto] = costoMinino
        return(costoMinino+arr[numSalto-1])
    else:
        costoMinino = min( generarMin(arr,numSalto+1, saltosMax, libroCostos) , generarMin(arr,numSalto+2, saltosMax, libroCostos))
        libroCostos[numSalto] = costoMinino
        return(costoMinino + arr[numSalto-1])

def solucionar(arr):
    libroCostos = {}
    saltosMax = len(arr)+1
    costoMinFinalUno = generarMin(arr, 1, saltosMax, libroCostos)
    costoMinFinalDos = generarMin(arr, 2, saltosMax, libroCostos)
    return(min(costoMinFinalUno, costoMinFinalDos))

def testear():
    casosPrueba = [
        [ 10, 15, 30],
        [20, 15, 10, 30, 12, 4, 3],
        [10, 20, 10, 5, 3, 1, 40, 80, 70],
        [1,100,1,1,1,100,1,1,100,1]
    ]

    salidas = [
        15,40,104,6
    ]

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = solucionar(casosPrueba[i])
            assert solution == salidas[i]
            print("ta bien")
        except Exception as error:
            print(f"Error, test {casosPrueba[i]}, expected {salidas[i]}, calculated {solution}", error)


testear()