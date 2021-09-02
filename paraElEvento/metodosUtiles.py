def solucionar():
    pass


def testear():
    casosPrueba = [
    ]

    salidas = [

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


def formatoCSAcademy():
    print("Formato para ejercicios en CSACADEMY")
    print("Ingresa los datos:")
    datos = list()
    entrada = ''
    while(entrada != 'art3'):
        entrada = input()
        if(entrada != 'art3'):
            datos.append(entrada)

    print('Ingreso de los datos')
    print(datos)
    numSep = int(input('De cuantas separaciones: '))
    miLista = list()

    for i in range(0, len(datos)+1-numSep, numSep):
        listaAux = list()
        for j in range(numSep):
            listaAux.append(datos[i+j])
        miLista.append(listaAux)

    print('Lista Formada:')
    print(miLista)


def formatoSEparadoPorComas():
    # ejemplo 1,3,5,7,8  --> ['1','3','5','7','8']
    entrada = input('Ingresa una lista separada por comas\n')
    entrada = entrada.replace(' ', '')
    miLista = entrada.split(',')
    print(miLista)
    otraL = list()
    for i in range(len(miLista)):
        otraL.append(True)
    print(otraL)


def main():
    formatoCSAcademy()


main()
