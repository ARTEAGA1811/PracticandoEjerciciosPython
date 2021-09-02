# https://csacademy.com/ieeextreme-practice/task/xtreme-rappers/

# def solucionar(a, b):
#     contador = 0
#     if(b>a):
#         aux = a
#         a = b
#         b = aux
#     while(True):
#         if(a >= 2 and b >= 1):
#             a = a-2
#             b = b-1
#             contador += 1
#         else:
#             if(a >= 1 and b >= 2):
#                 a = a-1
#                 b = b-2
#                 contador += 1
#             else:
#                 break

#     return contador


def solucionar(x,y):
    a = max(x,y)
    b = min(x,y)
    if(a-b)>=b:
        return b
    else:
        saltos = a-b
        aux = (a - saltos*2)
        ex = aux%3 == 0 
        aux = int(aux/2)
        saltos+=aux
        saltos+=int(aux/2)
      
        return saltos



def testear():
    casosPrueba = [
        [4,3],
        [0, 10000000000],
        [18,9],
        [5,5],
        [9,9],
        [0,10000000000],
        [10,10]
    ]

    salidas = [
        2, 0, 9,3,6,0,6
    ]

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = solucionar(casosPrueba[i][0], casosPrueba[i][1])
            assert solution == salidas[i]
            print("respuesta correcta")
        except Exception as error:
            print(
                f"Error, test {casosPrueba[i]}, expected {salidas[i]}, calculated {solution}", error)

testear()