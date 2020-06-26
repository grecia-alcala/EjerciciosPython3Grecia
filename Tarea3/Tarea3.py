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
    data = ["Nombre: ", mostrar.nombre(),"Apellido: ", mostrar.apellido(),"Numero de estudiante: ", mostrar.numero(),"Correo: ", mostrar.correo(),"Grupo: ", mostrar.grupo()]

    #fichero = open('Estudiantes.pickle')
    #fichero.write(data)
    #fichero.close()

    with open('Estudiantes.pickle', 'wb') as f:
        pickle.dump(data, f)
    f.close()


def Mostrar():

    with open("Estudiantes.pickle", "rb") as f:
        print(pickle.load(f))
    f.close()

def Modificar():
    pass

def OPC():
    print("1-Ingresar estudiante")
    print("2-Mostrar estudiantes")
    print("3-Modificar")
    print("4-Salir")
    i = int(input("Ingresar opcion: "))

    if i == 1:
        Guardar()
        return OPC()
    elif i == 2:
        Mostrar()
        return OPC()
    elif i == 3:
        Modificar()
        return OPC()
    else:
        pass

OPC()

