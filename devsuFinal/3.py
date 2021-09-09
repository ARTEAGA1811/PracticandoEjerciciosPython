def solucionar(arr):
    tamArr = len(arr)
    if(tamArr == 1):
        return arr[0]
    if(tamArr == 2 or tamArr ==3):
        return(max(arr))
    #aqui ya empiezo a anilizar.
    #al inicio.
    sumaMax = arr[0]+arr[2]
 
    for i in range(tamArr-2):  
        for k in range(i+2, tamArr):
            valor = arr[i]
            if(i == 0 and k == tamArr-1): #excepciop
                continue
            valor += arr[k]  
            if valor>sumaMax:
                sumaMax = valor

    return sumaMax
        


        




def testear():
    casosPrueba = [
        # [1,2],
        # [2,1,3],
        # [1,2,7,4,2],
        [99,34,50,32,61,16,55,29,68,17,77,58,60,24,9,13,93,55,68,63,70,41,37,38,93,68,43,35,40,51,74,26,78,21,25,42,18,0,17,36,55,53,61,28,4,79,71,47,98,57,33,89,41,16,19,13,53,69,21,81,28,11,64,19,55,29,27,8,77,14,75,16,54,12,20,97,31,9,4,63,83,44,42,81,87,4,50,28,60,96,54,51,23,70,61,10,19,48,71,20],
        [78,11,69,38,77,78,6,11,80,95,10,18,39,2,46,5,75,80,65,40,5,93,22,16,31,99,45,38,72,71,57,36,26,78,47,52,6,7,97,57,24,79,5,94,79,97,23,44,66,43,37,68,18,20,96,49,49,69,28,92,34,21,97,75,11,49,22,81,80,14,61,59,55,73,26,73,93,72,95,81,71,99,76,11,83,71,91,18,40,15,27,99,61,29,88,50,81,57,36,81]
        
    ]

    salidas = [
        # 2,3,9,
        197,198
    ]

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