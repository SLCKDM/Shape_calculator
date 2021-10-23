import shapes as ts
import unittest


class UnitTests(unittest.TestCase):

    global flat_shapes
    flat_shapes = [ts.Circle, ts.Square, ts.Rhombus,
                   ts.Rectangle, ts.Trapezoid, ts.Triangle]

    def setUp(self):
        """ Setup values for shapes """
        self.circle = ts.Circle(5)
        self.square = ts.Square(10)
        self.rhombus = ts.Rhombus(9, 3)
        self.rectangle = ts.Rectangle(5, 4)
        self.trapezoid = ts.Trapezoid(4, 5, 4, 15, 4.5)
        self.triangle = ts.Triangle(4, 4, 3)
        self.flat_examples = [self.circle, self.square, self.rhombus,
                              self.rectangle, self.trapezoid, self.triangle]

    def test_subclass(self):
        """ Checking if the subclass of the shape is correct """
        for shape in flat_shapes:
            actual = issubclass(shape,
                                ts.Flat)
            expected = True
            self.assertEqual(
                actual, expected,
                f'''Expected {shape.__name__} class
                to be a subclass of the Flat class.'''
            )

    def test_distinct_classes(self):
        """ Checking if the subclass of the shape is correct """
        for shape in flat_shapes:
            actual = shape is not ts.Volumetric
            expected = True
            self.assertEqual(
                actual, expected,
                f'''Expected {shape.__name__} class to
                be a distinct class from the Volumeric class.'''
            )

    def test_area(self):
        """ Check area for flat shapes """
        res = [78.53981633974483, 100, 27, 20, 45.0, 5.562148865321747]
        for ind, shape in enumerate(self.flat_examples):
            self.assertEqual(shape.area(), res[ind])

    def test_perimeter(self):
        """ Check perimeter for flat shapes """
        res = [31.41592653589793, 40, 36, 18, 28, 11]
        for ind, shape in enumerate(self.flat_examples):
            self.assertEqual(shape.perimeter(), res[ind],
                             f'''{shape._title} should be {res[ind]},
                             got {shape.area()}''')

    def test_circle_diameter(self):
        """ Check circle diameter """
        res = 10
        shape = self.circle
        self.assertEqual(shape.diameter(), res,
                         f'''{shape._title} should be {res},
                         got {shape.diameter()}''')

    def test_diagonal(self):
        """ Check square and rhombus diagonals """
        shapes = [self.square, self.rhombus]
        res = [14.142135623730951, 12.727922061357857]
        for i, shape in enumerate(shapes):
            self.assertEqual(shape.diagonal(), res[i],
                             f'''{shape._title} should be {res[i]},
                             got {shape.diagonal()}''')

    def test_mid_line(self):
        """ Check trapezoid middle line """
        res = 10
        shape = self.trapezoid
        self.assertEqual(shape.mid_line(), res,
                         f'''{shape._title} should be {res},
                         got {shape.mid_line()}''')

    def test_triangle_third_height(self):
        """ Check triangle third height """
        res = 3.7080992435478315
        shape = self.triangle
        self.assertEqual(shape.height, 3.7080992435478315,
                         f'''{shape._title} should be {res},
                         got {shape.height}''')


if __name__ == '__main__':
    unittest.main()
