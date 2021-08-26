print("Formato para ejercicios en CSACADEMY")
print("Ingresa los datos:")
datos = list()
entrada = ''
while(entrada != 'art3'):
    entrada = input()
    if(entrada !='art3'):
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