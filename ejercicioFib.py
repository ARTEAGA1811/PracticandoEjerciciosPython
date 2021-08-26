def calcularFibOptimizado(num):
    nmenosDos = 1
    nmenosUno = 2
    resultado = 0
    if(num == 0 or num == 1 or num == 2):
        return num

    for i in range(3, num+1, 1):
        resultado = nmenosUno + nmenosDos
        nmenosDos = nmenosUno
        nmenosUno = resultado
    return resultado


t = int(input())
for i in range(t):
    m = int(input())
    sobrevivientes = (calcularFibOptimizado(m) % 10)
    print(sobrevivientes)
