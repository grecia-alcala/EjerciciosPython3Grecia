class Figura():

    altura = int(input('Ingresar altura triangulo:'))
    base = int(input('Ingresar base triangulo:'))
    lado1 = int(input('Ingresar primer lado del triangulo:'))
    lado2 = int(input('Ingresar segundo lado del triangulo:'))
    lado3 = int(input('Ingresar tercer lado del triangulo:'))
    alturaR = int(input('Ingresar altura rectangulo:'))
    baseR = int(input('Ingresar base triangulo rectangulo:'))

    def __init__(self, altura, base, lado1, lado2, lado3, alturaR, baseR):

        self.altura = altura
        self.base = base
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

        self.alturaR = alturaR
        self.baseR = baseR

    def areaFigura(self):
        Triangulo.areaFigura(Triangulo)
        Rectangulo.areaFigura(Rectangulo)

    def perimetroFigura(self):
        Triangulo.perimetroFigura(Triangulo)
        Rectangulo.perimetroFigura(Rectangulo)


class Triangulo(Figura):


    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def areaFigura(self):
        print('Area triangulo: ', self.base * self.altura / 2)

    def perimetroFigura(self):
        print('Perimetro triangulo: ',self.lado1 + self.lado2 + self.lado3)

class Rectangulo(Figura):
    def __init__(self, alturaR, baseR):

        self.alturaR = alturaR
        self.baseR = baseR

    def areaFigura(self):
        print('Area Rectangulo: ', self.base * self.altura)

    def perimetroFigura(self):
        print('Perimetro Rectangulo: ', 2 * self.base + 2 * self.altura)


Figura.areaFigura(Figura)
Figura.perimetroFigura(Figura)