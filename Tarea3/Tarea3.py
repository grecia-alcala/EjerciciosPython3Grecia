import pickle
from pickle import Pickler


class Estudiante():

    def __init__(self):
        self.__Nombre = str(input('Nombre: '))
        self.__Apellido = str(input('Apellido: '))
        self.__NumeroEst = int(input('Numero Estudiante: '))
        self.__Correo = str(input('Correo: '))
        self.__Grupo = str(input('Grupo: '))

    def nombre(self):
        return self.__Nombre

    def apellido(self):
        return self.__Apellido

    def numero(self):
        return self.__NumeroEst

    def correo(self):
        return self.__Correo

    def grupo(self):
        return self.__Grupo


def Guardar():
    mostrar = Estudiante()
    ips = []

    for i in ips:
        print(i)

    bin = pickle.dumps(ips)
    print(bin)

    file = open('Estudiante.txt', 'wb')
    p = Pickler(file)
    p.dump(mostrar.nombre()), p.dump(mostrar.apellido())
    p.dump(mostrar.numero()), p.dump(mostrar.correo()), p.dump(mostrar.grupo())
    file.close()


def Mostrar():
    mostrar = Estudiante()

    print('Mi nombre es ', mostrar.nombre())
    print('Mi apellido es ', mostrar.apellido())
    print('Mi numero de estudiante es ', mostrar.numero())
    print('Mi correo es ', mostrar.correo())
    print('Mi grupo es ', mostrar.grupo())


def Modificar():
    pass

def OPC():
    print("1-Ingresar estudiante")
    print("2-Mostrar estudiantes")
    print("3-Modificar")
    i = int(input("Ingresar opcion: "))

    if i == 1:
        Guardar()
        return OPC()
    elif i == 2:
        Mostrar()
        return OPC()
    else:
        pass

OPC()