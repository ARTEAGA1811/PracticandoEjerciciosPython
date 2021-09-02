
def solucion(arr):
    if(len(arr) == 0 or len(arr) == 1):
        return(0)
    elif(len(arr) == 2):
        return(min(arr))
    else:
        costo = 0
        miCon = 0
        while(miCon<(len(arr)-1)):
            try:
                if(arr[miCon] == 0):
                    miCon+=1
                elif(arr[miCon] == arr[miCon+1]):
                    costo+=arr[miCon+1]
                    miCon+=2
                elif((arr[miCon]+arr[miCon+2])<= arr[miCon+1]):
                    costo+=(arr[miCon]+arr[miCon+2])
                    miCon+=3
                else:
                    costo+=arr[miCon+1]
                    miCon +=2 
            except:
                if(arr[-1]<=arr[-2]):
                    costo+=arr[-1]
                else:
                    costo+=arr[-2]
                break
        return(costo)
def testear():
    casosPrueba = [
        [10, 15, 30],
        [10, 50, 2, 1, 8, 9],
        [20, 15, 10, 30, 12, 4, 3],
        [10, 20, 10, 5, 3, 1, 40, 80, 70],
        [1,100,1,1,1,100,1,1,100,1],
        [0,1,2,2]
        ]

    casosPruebae =  [['-250 7', '9 1 2 3 4 5 -14']]
       
    salidas = [15,20,40,0,6,2]
    salidase = ['-400 2']     

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = solucion(casosPrueba[i])
            assert solution == salidas[i]
            print("ta bien")
        except Exception as error:
            print(f"Error, test {casosPrueba[i]}, expected {salidas[i]}, calculated {solution}", error)

testear()

