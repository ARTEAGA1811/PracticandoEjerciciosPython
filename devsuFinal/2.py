def solucionar(numSalto, maxSalto, arr):
    if(numSalto >= maxSalto):
        return True
    
    if(arr[numSalto] == 0):
        return False
    
    #casos recursivos
    vale = False
    for i in range(arr[numSalto]):
        vale = vale or solucionar(numSalto+i+1, maxSalto, arr)
    return vale

def testear():
    casosPrueba = [
        [3,1,1,1],
        [1,0,1],
        [2,5,5,2,5,3,4,0,5,1,0,4,3,2,0,1,1,4,3,0,2,3,1,5,3,5,2,2,1,5,2,5,4,2,4,2,4,0,3,5,2,1,5,1,0,0,4,3,2,4,4,5,0,3,1,4,0,2,1,4,1,0,4,3,5,5,1,5,4,0,2,1,5,2,4,3,5,2,1,2,0,5,2,4,2,1,2,4,5,4,1,0,0,3,3,5,2,0,0,0],
        [5,2,5,5,4,1,3,1,2,0,0,0,0,4,0,3,0,4,4,1,3,3,5,1,5,5,4,4,2,3,0,3,3,1,0,5,2,4,2,1,0,1,4,3,3,5,1,3,5,4,1,2,0,4,2,2,0,1,2,5,4,5,4,4,0,4,0,1,0,5,3,1,1,4,5,3,1,0,5,1,5,5,3,3,2,0,3,4,0,1,5,0,4,2,2,0,3,2,3,2]
    ]

    salidas = [
        True, False,True,False
    ]

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = solucionar(0,len(casosPrueba[i])-1,casosPrueba[i])
            assert solution == salidas[i]
            print("respuesta correcta")
        except Exception as error:
            print(
                f"Error, test {casosPrueba[i]}, expected {salidas[i]}, calculated {solution}", error)

testear()