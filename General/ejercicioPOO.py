
class Estudiante:
    # aca van los atributos de la clase, a qui se recomienda que vayan los atributos que sean constantes.
    def __init__(self, nombr, apellid): #Lo que esta en el init son atributos de cada objeto objeto //esto es como el constructor
        self.nombre = nombr
        self.apellido = apellid

    def saludarEstudiante(self, apodo):
        print('Hola ' + self.nombre + ' '+ self.apellido + ' tu apodo es: ' + apodo)
        return

    def __str__(self) -> str:
        return 'Jejejje que pendejo/a eres ' + self.nombre


#######################################################
e1 = Estudiante('', '')
e1.nombre = 'David'
e1.apellido = 'Arteaga'
e1.semestre = 4


e2 = Estudiante('Carla', 'Garcia')



print(e1.nombre,e1.apellido)
print(e2.nombre, e2.apellido)


e1.saludarEstudiante('Art3')
e2.saludarEstudiante('XD')

print(e1) #cuando se manda a imprimir el objeto, se imprime por degecto su posicion de memoria, al menos que le
print(e2) # hayamos creado un __str__ antes



