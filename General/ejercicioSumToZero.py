entrada = '[3,4,-7,5,-6,2,5,-1,8]'
datos = list()
for i in range(len(entrada)):
    if(entrada[i].isdigit()):
        if(entrada[i-1] == '-'):
            datos.append(int(entrada[i])*-1)
        else:
            datos.append(int(entrada[i]))

print(datos)  
sumatoria  = 0
indice = 0

while(indice<len(datos)):
    for i in range(len(datos)):
        sumatoria +=datos[i]
        if(sumatoria == 0):
            for j in range(i+1):
                datos.pop(0)
            sumatoria = 0
            indice = 0
            break
    
        indice+=1

print(datos)




