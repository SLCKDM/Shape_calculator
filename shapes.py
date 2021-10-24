import math


class Shape:
    """ class that represent shape and which is
    the parent for flat and volumeric shapes
    """
    _title = "Shape"
    _shapes = []

    def area(self):
        """method for all shapes that calculate area"""
        return NotImplemented


class Flat(Shape):
    """Shape subclass, which is parent for such shapes as:
    Circle, Square, Rhoumbus, Rectangle, Trapezoid, Triangle
    """
    _title = "Flat shape"

    def perimeter(self):
        """specific method for flat shapes that
        calculate perimeter of the Flat shapes"""
        return NotImplemented


class Volumetric(Shape):
    """sphere, cube, parallelepiped, pyramid, cylinder, cone"""
    _title = "Volumetric shape"

    def volume(self):
        """specific method for volumeric shapes of the Volumeric shapes"""
        return NotImplemented


class Circle(Flat):
    """Flat shape subclass

    Args:
        radius (int): arg which is needed to calculate
        area, perimeter and diameter of the Circle

    Methods:
        area: calculate area of the circle (r^2 * pi)
        perimeter: calculate perimeter of the circle (2 * pi * r)
        diameter: calculate diameter of the circle (r * 2)
    """
    _title = "Circle"

    def __init__(self, radius: int):
        super().__init__()
        self.radius = radius

    def area(self):
        return (self.radius ** 2) * math.pi

    def perimeter(self):
        return 2 * math.pi * self.radius

    def diameter(self):
        """ return diameter of shape"""
        return self.radius * 2


class Square(Flat):
    """Flat shape subclass

    Args:
        a (int): side of the square. Arg which is needed to
        calculate area, perimeter and diagonal of the Square

    Methods:
        area: calculate area of the square (a^2)
        perimeter: calculate perimeter of the square (a * 4)
        diagonal: calculate diameter of the square (a * sqrt(2))
    """
    _title = "Square"

    def __init__(self, a: int):
        super().__init__()
        self.a = a

    def area(self):
        return self.a ** 2

    def perimeter(self):
        return self.a * 4

    def diagonal(self):
        """ return diagonal(int) of square or rhombus """
        return self.a * math.sqrt(2)


class Rhombus(Square):
    """Flat shape subclass

    Args:
        a (int): side of the rhombus
        height (int): of the rhombus
    Methods:
        area: calculate area of the rhombus (a * height)
        perimeter: calculate perimeter of the rhombus (a * 4)
        diagonal: calculate diameter of the rhombus (a * sqrt(2))
    """
    _title = "Rhombus"

    def __init__(self, a: int, height: int):
        super().__init__(a)
        self.a = a
        self.height = height

    def area(self):
        return self.a * self.height


class Rectangle(Square):
    """Flat shape subclass

    Args:
        a|b (int): sides of the rectangle
    Methods:
        area: calculate area of the rectangle (a * b)
        perimeter: calculate perimeter of the rectangle (a * 2 + b * 2)
        diagonal: calculate diameter of the rectangle (a * sqrt(2))
    """
    _title = "Rectangle"

    def __init__(self, a: int, b: int):
        super().__init__(b)
        self.a = a
        self.b = b

    def area(self):
        return self.a*self.b

    def perimeter(self):
        return self.a*2 + self.b*2

    def diagonal(self):
        return math.sqrt(self.a**2 + self.b**2)


class Trapezoid(Flat):
    """Flat shape subclass

    Args:
        a|b|c|d (int): sides of the trapezoid
        height (int): height of the trapezoid
    Methods:
        area: calculate area of the trapezoid (mid_line * height)
        perimeter: calculate perimeter of the trapezoid (a + b + c + d)
        mid_line: calculate middle line of the trapezoid ((a+b)/2)
    """
    _title = "Trapezoid"

    def __init__(self, a: int, b: int, c: int, d: int, height: int):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.height = height

    def area(self):
        return self.mid_line()*self.height

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def mid_line(self):
        """ return middle line value of trapezoid"""
        return (self.d+self.b)/2


class Triangle(Flat):
    """Flat shape subclass

    Args:
        a|b|c (int): sides of the triangle
    Methods:
        area: calculate area of the triangle (1/2 * c * height)
        perimeter: calculate perimeter of the triangle (a + b + c)
        height: calculate height of the triangle (2*sqrt(p(p-a)*(p-b)(p-c)))/2
    """
    _title = "Triangle"

    def __init__(self, a: int, b: int, c: int):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    @property
    def _p(self):
        """ return half of perimeter """
        return 0.5*(self.a+self.b+self.c)

    def area(self):
        return 0.5 * self.c * self.height

    def perimeter(self):
        return self.a + self.b + self.c

    def height(self):
        """ return height of the shape """
        p = self._p
        return (2*math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c)))/self.c


class Sphere(Volumetric):
    """Volumeric shape subclass

    Args:
        radius (int): radius of the sphere
    Methods:
        area(): calculate area of the sphere (4 * pi * radius^2)
        volume(): calculate volume of the sphere (4/3 * pi * radius^3)
        diameter(): calculate radius of the sphere (radius*2)
    """
    _title = "Sphere"

    def __init__(self, radius: int):
        super().__init__()
        self.radius = radius

    def area(self):
        return 4 * math.pi * self.radius**2

    def volume(self):
        return 4/3 * math.pi * self.radius**3

    def diameter(self):
        """ return sphere diameter """
        return self.radius * 2


class Cube(Volumetric):
    """Volumeric shape subclass

    Args:
        a (int): side of the cube
    Methods:
        area(): calculate area of the cube (6 * a^2)
        volume(): calculate volume of the cube (a^3)
        diagonal(): calculate diagonal of the cube (sqrt(3)*a)
    """
    _title = "Cube"

    def __init__(self, a: int):
        super().__init__()
        self.a = a

    def area(self):
        return 6*(self.a**2)

    def volume(self):
        return self.a**3

    def diagonal(self):
        """ diagonal of the cube """
        return math.sqrt(3)*self.a


class Parallelepiped(Volumetric):
    """Volumeric shape subclass

    Args:
        a|b|c (int): sides of the  parallelepiped
    Methods:
        area(): calculate area of the parallelepiped (2(a * b + b * c + a * c))
        volume(): calculate volume of the parallelepiped (a * b * c)
        diagonal(): calculate diagonal of the parallelepiped (a^2 + b^2 + c^2)
    """
    _title = "Parallelepiped"

    def __init__(self, a: int, b: int, c: int):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        return 2*(self.a*self.b + self.b*self.c + self.a*self.c)

    def volume(self):
        return self.a*self.b*self.c

    def diagonal(self, square: bool = None):
        """ return diagonal of the parallelepiped

        bool = True let function return square of diagonal
        """
        _expression = self.a**2+self.b**2+self.c**2
        if square:
            return _expression
        else:
            return math.sqrt(_expression)


class Pyramid(Volumetric):
    """Volumeric shape subclass

    Args:
        edge (int): sides of the pyramid
        radius (int): sides of the pyramid
        *sides (int): sides of the pyramid
    Methods:
        area(): calculate area of the pyramid (n * a/2 * apothema)
        volume(): calculate volume of the pyramid ()
        height(): calculate height of the pyramid (sqrt(edge^2 - radius^2))
        apothema(): calculate apothema of the pyramid
        (sqrt(height+(a/(2*tan(180/n)))^2))
    """
    _title = "Pyramid"

    def __init__(self, edge: int, radius: int, *sides: int):
        super().__init__()
        self.edge = edge
        self.radius = radius
        self.sides = sides

    @property
    def _n(self):
        """ Return quantity of sides"""
        return len(self.sides)

    @property
    def _a(self):
        """ Return side length """
        return self.sides[0] if len(set(self.sides)) == 1 else None

    def height(self):
        """ calculate and return height of the pyramid"""
        return math.sqrt(self.edge**2 - self.radius**2)

    def apothem(self):
        """ calculate and return apothem of the pyramid"""
        return math.sqrt(self.height()+(self._a/(2*math.tan(180/self._n)))**2)

    def volume(self):
        if self._n == 1:
            base = Square(self.sides[0])
            return 1/3 * base.area() * self.height()
        elif self._n == 3:
            if self.sides[0] == self.sides[1] == self.sides[2]:
                a = self.sides[0]
                return (math.sqrt(3) * a**2 * self.height())/12
        elif (self._n == 6) and (len(set(self.sides)) == 1):
            return (3 * math.sqrt(3) * self.sides[0] * self.height())/6

    def area(self):
        return (self._n*self._a/2) * self.apothem()


class Cylinder(Volumetric):
    """Volumeric shape subclass

    Args:
        radius (int): sides of the cylinder
        height (int): sides of the cylinder

    Methods:
        area(): calculate area of the cylinder (2 * pi * radius * height)
        volume(): calculate volume of the cylinder (base_area * height)
    """
    _title = "Cylinder"

    def __init__(self, radius: int, height: int):
        super().__init__()
        self.radius = radius
        self.height = height

    def area(self, __side: bool = None):
        """ calculate and return area of the cylinder

        __side=True to calculate side area of the cylinder
        """
        if __side:
            return 2 * math.pi * self.radius*self.height
        else:
            return 2 * math.pi * self.radius*(self.radius+self.height)

    def volume(self):
        base = Circle(self.radius)
        return base.area() * self.height


class Cone(Volumetric):
    """Volumeric shape subclass

    Args:
        radius (int): sides of the cone
        height (int): sides of the cone

    Methods:
        area(): calculate area of the cone (pi * radius * (radius * slant_h))
        volume(): calculate volume of the cone (1/3 * pi * radius^2 * height)
    """
    _title = "Cone"

    def __init__(self, radius: int, height: int):
        super().__init__()
        self.radius = radius
        self.height = height

    def slant_height(self):
        return math.sqrt(self.radius**2 + self.height**2)

    def area(self, _side: bool = None):
        """ specific method to calculate area of shape

        __side = True to calculate side area
        """
        if _side:
            return math.pi*self.radius*self.slant_height()
        else:
            return math.pi*self.radius*(self.radius*self.slant_height())

    def volume(self):
        return 1/3*math.pi*(self.radius**2)*self.height


if __name__ == "__main__":
    pass
