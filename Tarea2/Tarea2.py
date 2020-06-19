import re

#verificacion de correo
def correoValido(correo):
    expresion = '[a-zA-Z0-9. ]{5,10}@[a-zA-Z0-9]*(\.[a-zA-Z0-9]*)?(\.[a-zA-Z0-9]{2,3}){1,2}$'
    return re.match(expresion, correo) is not None

correos = [str(input("ingresar correo: "))]

for correo in correos:
    print("Probando si '{}' es válido...{}".format(correo, correoValido(correo)))

#verificacion de nuemro
def numeroTelefono(numero):
    exNum = '[0-9]{10}|\([0-9]{2,3}\)[0-9]{7,8}|\([0-9]{2,3}\)[ -]?[0-9]{3,4}[ -]?[0-9]{4}$'
    return re.match(exNum, numero) is not None

tels = ['(33)12345678']

for numero in tels:

    print("verificando si '{}' es valido...{}".format(numero, numeroTelefono(numero)))