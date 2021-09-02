#entrada = '0 1 0 2 1 0 1 3 2 1 2 1'
#entrada = '4 2 0 3 2 5'
#entrada = list(entrada.split())
#datos = list()
#for i in entrada:
#    datos.append(int(i))

entrada = '[4,2,0,3,2,5]'
datos = list()
for i in entrada:
    if( i.isdigit()):
        datos.append(int(i))

posParedInicio = 0
posParedFinal = 0

sumAgua = 0
saltoAOtraPared = 0

for i in range(len(datos)):
    if(datos[i]>0):
        posParedInicio = i
        break

for i in range(len(datos)-1, -1, -1):
    if(datos[i]>0):
        posParedFinal = i
        break
    # print(datos[i], end=' ')


if(posParedInicio == posParedFinal):
    print(0)
else:
    #aqui empieza el juego jaj
    for i in range(posParedInicio, posParedFinal+1, 1):

        if(i<saltoAOtraPared):
            continue
        elif(i == posParedFinal): 
            break
        elif(datos[i+1] >= datos[i]): 
            continue
        else:
            #busca otro igual o mas alto
            hayMasAlto = False
            posmasAlto = i+1
            for x in range(i+1, posParedFinal+1, 1):
                if(datos[x]>= datos[i]):
                    hayMasAlto = True
                    posmasAlto = x
                    break
                        
            if(hayMasAlto):
                #llena todos los espacios
                for bucle in range(i+1, posmasAlto, 1):
                    sumAgua +=(datos[i]-datos[bucle])
                
                #paso directo a esta pared y me salto todos los espacios donde llene el agua
                saltoAOtraPared = posmasAlto
            else:
                #busco en los siguientes quien es mas alto
                posSiguienteAlto = i+1
                for bucle in range(i+1, posParedFinal+1, 1):
                    if(datos[bucle] > datos[posSiguienteAlto]):
                        posSiguienteAlto = bucle
                
                #esta al lado?
                if(i+1 == posSiguienteAlto):
                    pass
                else:
                    #lleno con agua al nivel de la pared de la derecha
                    for bucle in range(i+1, posSiguienteAlto, 1):
                        sumAgua+=(datos[posSiguienteAlto]-datos[bucle])
                
                    #tengo que pasar a esta pared
                    saltoAOtraPared = posSiguienteAlto
            

print(sumAgua, end='')