class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def area(self):
        return self.width * self.height

def print_area(r):
    area = r.area()
    print(f"The area is {area}")


r = Rectangle(2, 3)
print_area(r)

s = Square(2)
print_area(s)  # Error: the area should be 4, but it's 8
