# def solucionar(n):
#     n = n-1
#     valor = 1
#     if(n == 0):
#         return 1
#     contador = 1
#     for i in range(1, n+1):
#         if(contador % 4 == 0):
#             #arr.append(arr[i-1]-1)
#             valor = valor-1
#             contador = 0
#         else:
#            #arr.append(arr[i-1]+1)
#            valor = valor+1
#         contador+=1
#     return valor

def solucionar(n):
    if(n>=1 and n<=4):
        return(n)
    else:
        numBajones = ((n-1) - ((n-1)%4))
        numBajones = int(numBajones/4)
    
        valor = n -(numBajones*2)
        return(valor)





def testear():
    casosPrueba = [
        1,6,77, 545421,4611686018327187,87123641123172368
    ]

    salidas = [
        1,4,39, 272711,0,0
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

#print(solucionar(21))