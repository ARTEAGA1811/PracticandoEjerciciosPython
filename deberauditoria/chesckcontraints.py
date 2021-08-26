fichero = open('deberauditoria\miArchivo.txt')
lineas = fichero.readlines()
salida = list()

for i in range(len(lineas)):
    lineas[i] = lineas[i].strip()
    

for i in lineas:
    print('DBCC CHECKCONSTRAINTS (\''+i+'\');')
