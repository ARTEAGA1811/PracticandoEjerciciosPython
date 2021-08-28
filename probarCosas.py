
#PARA SEPARAR CUANDO SOLO SON NUMEROS POSITIVOS ENTEROS
# entrada = input()
# datos = list()
# for i in entrada:
#     if( i.isdigit()):
#         datos.append(int(i))

# print(datos)


#PARA SEPARAR CUANDO HAY NUMEROS CON SIGNO
# entrada = entrada = '[4,-2,0,3,2,5]'
# datos = list()
# for i in range(len(entrada)):
#     if(entrada[i].isdigit()):
#         if(entrada[i-1] == '-'):
#             datos.append(int(entrada[i])*-1)
#         else:
#             datos.append(int(entrada[i]))




# cadena = '999999'
# num = len(re.findall('(?=99)', cadena))

# otro = re.findall('(?=99)', cadena)

# for i in otro:
#     print(i)
#matches_positions = [match.start() for match in num]
#rint(matches_positions)


# cadena = '999999'
# miL = []
# for i in range(len(cadena)):
#     if(cadena.startswith('99', i)):
#         miL.append(i)

# print(miL)



libro = {1:12, 2:13, 3:14}

if ( 5 in libro):
    print('si')
else:
    print('no')