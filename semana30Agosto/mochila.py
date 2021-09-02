def solucionar(n, C, pes, gan, result):
    if n == 0 or C == 0 : #llego al final de la lista o la capacidad llega a cero
        return result
    elif(pes[n-1]>C):
        solucionar(n-1, C, pes, gan, result)
    else:
        tmpUno  = solucionar(n-1, C, pes, gan, result)
        tmpDos = max(solucionar(n-1, C-pes[n-1], gan, result), 
        

    





t = int(input())

for i in range(t):
    entr = input().split()
    cap = int(entr[0])
    n = int(entr[1])
    gan = []
    peso = []
    for k in range(n):
        e = input().split()
        peso.append(int(e[0]))
        gan.append(int(e[1]))
    
    solucionar(n, cap, peso, gan)



