import re

# No letras
def noLetras(texto):
    nl = '[^a-zA-Z]$'
    return re.match(nl, texto) is not None

print("verificando que no se tengan letras")
letras = [str(input("ingresar: "))]

for texto in letras:
    print("Probando si '{}' no tiene letras...{}".format(texto, noLetras(texto)))

# Solo Numeros
def soloNumeros(texto):
    sn = '\d+$'
    return re.match(sn, texto) is not None

print("verificacion de solo numeros")
numeros = [str(input("ingresar:"))]

for texto in numeros:
    print("Probando si '{}' son numeros...{}".format(texto, soloNumeros(texto)))

# Solo mayusculas
def soloMayusculas(texto):
    sM = '[A-Z]+$'
    return re.match(sM, texto) is not None

print("verificacion de solo mayusculas")
mayusculas = [str(input("ingresar: "))]

for texto in mayusculas:
    print("Probando si '{}' son mayusculas...{}".format(texto, soloMayusculas(texto)))

# Solo minusculas
def soloMinusculas(texto):
    sm = '[a-z]+'
    return re.match(sm, texto) is not None

print("verificacion de solo minusculas")
minusculas = [str(input("ingresar: "))]

for texto in minusculas:
    print("Probando si '{}' son minusculas...{}".format(texto, soloMinusculas(texto)))

# No numeros
def noNumeros(texto):
    nn = '[^0-9]$'
    return re.match(nn, texto) is not None

print("verificando que no se tengan numeros")
numeros = [str(input("ingresar: "))]

for texto in numeros:
    print("Probando si '{}' no tiene numeros...{}".format(texto, noNumeros(texto)))
