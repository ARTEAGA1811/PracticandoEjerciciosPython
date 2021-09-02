def solucionar(arr: list):
    aux = []
    cont = 0
    i = 0
    while(cont <len(arr)):
        if(arr[i] == 0):
            aux.append(0)
            aux.append(0)
            cont+=2
        else:
            aux.append(arr[i])
            cont+=1
        i+=1
    arr = aux.copy()
    return(arr)
        


def testear():
    casosPrueba = [
       [1,0,2,3,0,4,5,0]
    ]

    salidas = [[1,0,0,2,3,0,0,4]]
    

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = solucionar(casosPrueba[i])
            assert solution == salidas[i]
            print("respuesta correcta")
        except Exception as error:
            print(
                f"Error, test {casosPrueba[i]}, expected {salidas[i]}, calculated {solution}", error)

testear()