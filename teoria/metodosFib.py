def calcularFibonnaci(num):
    #0:0 1:1 2:2 3:3 4:5 5:8
    liFib = list()
    liFib.append(0)
    liFib.append(1)
    liFib.append(2)

    for i in range(3, num+1, 1):
        liFib.append(liFib[i-1]+liFib[i-2])
    
    return liFib[num]


def calcularFibOptimizado(num):
    nmenosDos = 1
    nmenosUno = 2
    resultado = 0
    for i in range(3, num+1, 1):
        resultado = nmenosUno + nmenosDos
        nmenosDos = nmenosUno
        nmenosUno = resultado
    
    if(num == 0 or num == 1 or num == 2):
        return num
    return resultado

print(calcularFibonnaci(5))