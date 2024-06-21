class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


rect = Rectangle(10, 20)
print(f'Площадь прямоугольника: {rect.area}')
