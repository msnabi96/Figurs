class Figura():

    def __init__(self, name):
        self.name = name

    def kvadrad(self, a):
        self.a = a
        s = a * a
        return print(f'Площадь фигуры {self.name} равна {s} см.')

    def pryamougol(self, a, b):
        self.a = a
        self.b = b
        s = a * b
        return print(f'Площадь фигуры {self.name} равна {s} см.')

    def krug(self, r):
        self.r = r
        s = r * r * 3.14
        return print(f'Площадь фигуры {self.name} равна {s} см.')

    def treug(self, a):
        self.a = a
        s = (a * a * (3 ** (0.5))) / 4
        return print(f'Площадь фигуры {self.name} равна {s} см.')


# Ниже объекты класса
kvadrat_1 = Figura('Квадрат')
pryamougol_1 = Figura('Прямоугольник')
krug_1 = Figura('Круг')
treug_1 = Figura('Треугольник')

# Ниже вызовы объектов
kvadrat_1.kvadrad(2)
pryamougol_1.pryamougol(4, 5)
krug_1.krug(3)
treug_1.treug(3)
