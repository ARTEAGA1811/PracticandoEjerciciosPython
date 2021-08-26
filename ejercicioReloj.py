import re
from datetime import datetime

# 12:00 17:30 blabla 20:21 26:88
ingreso = '12:00 17:30 blabla 20:21 26:88'
cadena = list(ingreso.split())
patron = '^([0-1]{1}[0-9]{1}|2[0-3]{1}):[0-5]{1}[0-9]{1}$'

sumatoria = float(0)
print(cadena)
for i in cadena:
    if(re.search(patron, i)):
        conversion = datetime.strptime(i, "%H:%M")
        conversion = str(conversion.strftime("%I:%M"))
        separador = conversion.split(sep=':')
        hh = int(separador[0])
        mm = int(separador[1])
        print(hh, mm)
        #conversion a grados
        gMin = float(6*mm)
        gHour = float((30*hh) + ((1/12)*gMin))

        if(gHour > gMin):
            sumatoria+=(360- gHour + gMin)
        elif(gMin > gHour):
            sumatoria+=(gMin - gHour)
        else:
            sumatoria+=0
    else:
        sumatoria-=100

print(sumatoria)
