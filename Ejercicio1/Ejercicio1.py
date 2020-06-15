def primero():
    print('Saber si un numero es positivo, negativo, cero, par o impar')
    numero = int(input('Escribe un numero: '))

    if numero > 0:
        print('El numero', numero, 'es positivo')
    elif numero < 0:
        print('El numero', numero, 'es negativo')
    else:
        print('El numero', numero, 'es cero')

    if numero % 2 == 0:
        print('El número', numero, 'es par')
    else:
        print('El número', numero, 'es impar')

def primo():
    print('Saber si un numero es primo')
    primo = int(input('Escribe un numero: '))

    valor = range(2,primo)
    contador = 0;

    for n in valor:
        if primo % n == 0:
            contador += 1

    if contador > 0:
        print('El número', primo, 'no es primo')
    else:
        print('El número', primo, 'es primo')


def bisiesto():
    print('Saber si un año es bisiesto')
    anio = int(input('Escribe un año: '))

    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        print('El año', anio, 'es bisiesto')
    else:
        print('El año', anio, 'no es bisiesto')

primero()
primo()
bisiesto()
