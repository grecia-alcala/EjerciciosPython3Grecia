def capturar():
    global lista
    lista = []
    print("Cuantos elemantos tendra la Lista")
    n = input()
    n = int(n)
    for i in range(0,n):
        print("Ingresar elemento ", i)
        elemento = input()
        lista.insert(i, elemento)

def mostrar():
    print(lista)
    for recorrido in range(1, len(lista)):
        for posicion in range(len(lista) - recorrido):
            if lista[posicion] > lista[posicion + 1]:
                temp = lista[posicion]
                lista[posicion] = lista[posicion + 1]
                lista[posicion + 1] = temp
    print('Lista ordenada:')
    print(lista)


capturar()
mostrar()