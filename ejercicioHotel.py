t = int(input())

for i in range(t):
    datosEntrada = input()
    datosEntrada = datosEntrada.split()
    
    m = int(datosEntrada[0])
    n = int(datosEntrada[1])
    k = int(datosEntrada[2])

    validosCadaPiso = list()
    for j in range(m):
        roomsCorrect = int(input())

        if(roomsCorrect >= 0 and roomsCorrect <= n):
            validosCadaPiso.append(roomsCorrect)
        else:
            validosCadaPiso.append(0)
        
    validosCadaPiso.sort()

    for a in range(k):
        validosCadaPiso[a] = n - validosCadaPiso[a]
    
    sumatoria = 0

    for b in validosCadaPiso:
        sumatoria+=b
    
    print(sumatoria)





 