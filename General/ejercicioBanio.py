#funciones
def calcNumPilas(n):
    if((n%10) == 0 ):
        return int(n/10)
    else:
        return int((n - (n%10) + 10) / 10)

#####################################
entradaDatos = input()
entradaDatos = entradaDatos.split()

numBat = int(entradaDatos[0])
precioBlack = int(entradaDatos[1])
precioPink = int(entradaDatos[2])

# depende los banios
datosCadaBanio = list()
for i in range(numBat):
    inDos = input()
    inDos = inDos.split()
    a = int(inDos[0])
    b = int(inDos[1])
    datosCadaBanio.append({'black': a, 'pink': b })

numBlack = 0
numPink = 0
for j in datosCadaBanio:
    numBlack += j['black']
    numPink += j['pink']

# ahora debo subirlos al superior y calcular la s pilas
numBlack = calcNumPilas(numBlack)
numPink = calcNumPilas(numPink)

precioTotal = (numBlack * precioBlack) + (numPink * precioPink)
print(precioTotal)








