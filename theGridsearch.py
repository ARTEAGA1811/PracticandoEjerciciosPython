import math
import os
import random
import re
import sys
def gridSearch(G, P):
    for i in range(len(G)-len(P)+1):  # para que cuadre
        arr = []
        for k in range(len(G[0])):
            if(G[i].startswith(P[0], k)):
                arr.append(k)
        if(len(arr) > 0):
            for buc in range(1, len(P)):  # voy por cada fila del patron
                for k in arr:  # analizo si el patron esta en las posiciones
                    if(P[buc] not in G[i+buc][k:(k+len(P[0]))]):
                        # elimino ese indice
                        arr.remove(k)
            #si tiene al menos un array significa que si esta el patron
            if(len(arr) > 0):
                return('YES')

    # acabo todas filas y no encontro
    return('NO')


#uno = ['7283455864', '6731158619', '8988242643', '3830589324', '2229505813', '5633845374', '6473530293', '7053106601', '0834282956', '4607924137']
#uno =['123456', '567890', '234567', '194729']
#uno = ['999999', '121211']
A1 = ['456712', '561245', '123667', '781288']  # YES
#dos = ['9505', '3845', '3530']
#dos = ['78', '67']
# dos=['99','11']
A2 = ['45', '67']
print(gridSearch(A1, A2))
