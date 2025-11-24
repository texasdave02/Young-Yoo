# PE07_1 - Method Overriding
# Adding full comments as required

import math

class Shape:
    """Base class for geometric shapes."""

    def computeArea(self):
        """Returns the area of a generic shape (default 0)."""
        return 0


class Rectangle(Shape):
    """Rectangle shape with width and height."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    # task: override computeArea()
    def computeArea(self):
        """Compute area of a rectangle."""
        return self.width * self.height


class Square(Shape):
    """Square shape with one side length."""

    def __init__(self, side):
        self.side = side

    # task: override computeArea()
    def computeArea(self):
        """Compute area of a square."""
        return self.side * self.side


class Triangle(Shape):
    """Triangle shape defined by three sides."""

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # task: override computeArea() using Heron's formula
    def computeArea(self):
        """Compute area of triangle using 3 sides."""
        s = (self.a + self.b + self.c) / 2.0  # semi-perimeter
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area


# ----------- Test Code -----------
rect = Rectangle(5, 10)
print("Rectangle area:", rect.computeArea())

square = Square(6)
print("Square area:", square.computeArea())

triangle = Triangle(3, 4, 5)
print("Triangle area:", triangle.computeArea())
