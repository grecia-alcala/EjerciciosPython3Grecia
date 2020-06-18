class Estudiante():

    def __init__(self):
        self.__Nombre = str(input('Nombre: '))
        self.__Correo = str(input('Correo: '))
        self.__Contrasenia = str(input('Contraseña: '))

    def nombre(self):
        return self.__Nombre

    def correo(self):
        return self.__Correo

    def contrasenia(self):
        return self.__Contrasenia

mostrar = Estudiante()

print('Mi nombre es ', mostrar.nombre())
print('Mi correo es ',mostrar.correo())
print('Mi contraseña es ',mostrar.contrasenia())

