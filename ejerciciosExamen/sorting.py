def invertir_cadena(cadena):
    return cadena[::-1]

def solucionar(cadena):
    arrStr = [str(i) for i in cadena]
    for j in range(len(arrStr)):
        aux = invertir_cadena(arrStr[j])
        arrStr[j] = aux
    #ordeno
    arrStr.sort()
    #regreso a la normalidad
    for j in range(len(arrStr)):
        aux = invertir_cadena(arrStr[j])
        arrStr[j] = int(aux)  
    return(arrStr)

def testear():
    casosPrueba = [
        [1, 10, 20, 33, 13, 60, 92, 100, 21]
    ]

    salidas = [
        [100, 10, 20, 60, 1, 21, 92, 13, 33]
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