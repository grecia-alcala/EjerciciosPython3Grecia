from mongoengine import *

connect(db = 'padts',host='localhost',port=27017)

class Estudiante(Document):
    nombre = StringField(required=True)
    apellido = StringField(required=True)
    numeroEst = IntField(required=True, unique = True)
    correo = StringField(required=True)
    grupo = StringField(required=True)

def AgregarEstudiante():
    Nombre = str(input('Nombre: '))
    Apellido = str(input('Apellido: '))
    NumeroEst = int(input('NumeroEst'))
    Correo = str(input('Correo: '))
    Grupo = str(input('Grupo: '))

    estudiante = Estudiante(
    nombre = Nombre,
    apellido = Apellido,
    numeroEst = NumeroEst,
    correo = Correo,
    grupo = Grupo
    )
    estudiante.save()

def LeerEstudiante(numero):
    estudiante = Estudiante.objects(numeroEst = numero)
    for a in estudiante:
        print(f'Nombre: {a.nombre}\nApellido: {a.apellido}\nNumero de Estudiante: {a.numeroEst}\
        \nCorreo: {a.correo}\nGrupo: {a.grupo}')

def ActualizarEstudiante(numero):
    estudiante = Estudiante.objects(numeroEst = numero)
    for a in estudiante:
        print(f'Nombre: {a.nombre}\nApellido: {a.apellido}\
        \nCorreo: {a.correo}\nGrupo: {a.grupo}')
    Nombre = str(input('Nombre: '))
    Apellido = str(input('Apellido: '))
    Correo = str(input('Correo: '))
    Grupo = str(input('Grupo: '))
    estudiante.update(nombre = Nombre,
    apellido = Apellido,
    correo = Correo,
    grupo = Grupo)
    estudiante = Estudiante.objects(numeroEst = numero)
    for a in estudiante:
        print(f'Nombre: {a.nombre}\nApellido: {a.apellido}\nNumero de Estudiante: {a.numeroEst}\
        \nCorreo: {a.correo}\nGrupo: {a.grupo}')


def EliminarEstudiante(numero):
    Estudiante.objects(numeroEst = numero).delete()
    estudiante = Estudiante.objects()
    for a in estudiante:
        print(f'Nombre: {a.nombre}\nApellido: {a.apellido}\nNumero de Estudiante: {a.numeroEst}\
        \nCorreo: {a.correo}\nGrupo: {a.grupo}')


def OPC():
    print("1-Ingresar estudiante")
    print("2-Leer estudiante")
    print("3-Actualizar estudiante")
    print("4-Eliminar estudiante")
    print("5-Salir")
    i = int(input("Ingresar opcion: "))

    if i == 1:
        AgregarEstudiante()
        return OPC()
    elif i == 2:
        num = int(input('Numero de estudiante a leer: '))
        LeerEstudiante(num)
        return OPC()
    elif i == 3:
        num = int(input('Numero de estudiante a actualizar: '))
        ActualizarEstudiante(num)
        return OPC()
    elif i == 4:
        num = int(input('Numero de estudiante a eliminar: '))
        EliminarEstudiante(num)
        return OPC()
    else:
        pass

OPC()
