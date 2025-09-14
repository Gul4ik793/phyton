import abc
class Shape(abc.ABC):
    @abc.abstractmethod 
    def area(self): pass

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self): return self.width * self.length

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area (self): return self.radius * self.radius * 3.14

class Triangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self): return self.width * self.height * 1/2

rect = Rectangle(1, 20)
print("Площадь прямоугольника:", rect.area())

circ = Circle(10)
print("Площадь круга:", circ.area())

tri = Triangle(10, 20)
print("Площадь треугольника:", tri.area())
