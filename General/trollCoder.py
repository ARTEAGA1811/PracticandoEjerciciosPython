
def enviarBits(miLista):
    mensaje = 'Q'
    for i in miLista:
        mensaje+= ' '+str(i)
        
    return mensaje

def cambiarBit(miLista, ind):
    if(miLista[ind] == 0):
        miLista[ind] = 1
    else:
        miLista[ind] = 0

def enviarRespuesta(miLista):
    mensaje = 'A'
    for i in miLista:
        mensaje+= ' '+str(i)
    return mensaje

##################################

k = int(input())

#creacion de la lista
misbits = list()
for i in range(k):
    misbits.append(0)
#lo envio
print(enviarBits(misbits))
correctos = int(input())

indice = 0
valorAnterior = correctos

if(k != correctos):
    #cambiamos
    cambiarBit(misbits, indice)
    print(enviarBits(misbits))
    correctos = int(input())

while(k != correctos):
    
    if(correctos > valorAnterior):
        #le dejo ahi
        indice+=1
        valorAnterior = correctos
        #ahora ya lo cambio
        cambiarBit(misbits,indice)
    else:
        #lo cambio
        cambiarBit(misbits, indice)
        valorAnterior= correctos
        correctos+=1

        indice+=1
        cambiarBit(misbits, indice)
 
    #lo mando
    print(enviarBits(misbits))

    #recibo feedback
    correctos = int(input())


print(enviarRespuesta(misbits)) 
        

