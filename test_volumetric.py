import shapes as ts
import unittest


class UnitTests(unittest.TestCase):

    global volumetric_shapes
    volumetric_shapes = [ts.Sphere, ts.Cube, ts.Parallelepiped,
                         ts.Pyramid, ts.Cylinder, ts.Cone]

    def setUp(self):
        """ Setup values for shapes """
        self.sphere = ts.Sphere(10)
        self.cube = ts.Cube(5)
        self.parallelepiped = ts.Parallelepiped(4, 5, 6)
        self.pyramid = ts.Pyramid(5, 4, 2)
        self.cylinder = ts.Cylinder(3, 5)
        self.cone = ts.Cone(4, 8)
        self.volumetric_examples = [
                                self.sphere, self.cube, self.pyramid,
                                self.parallelepiped, self.cylinder, self.cone
                                    ]

    def test_subclass(self):
        """ Checking if the subclass of the shape is correct """
        for shape in volumetric_shapes:
            actual = issubclass(shape,
                                ts.Volumetric)
            expected = True
            self.assertEqual(
                actual, expected,
                f'Expected {shape.__name__} class to be \
                a subclass of the Volumetris class.'
            )

    def test_distinct_classes(self):
        """ Checking if the subclass of the shape is correct """
        for shape in volumetric_shapes:
            actual = shape is not ts.Flat
            expected = True
            self.assertEqual(
                actual, expected,
                f'Expected {shape.__name__} class to be \
                a distinct class from the Flat class.'
            )

    def test_volume(self):
        """ Check volume of every volumetric shape """
        res = [4188.790204786391, 125, 120, 4.0,
               141.3716694115407, 134.0412865531645]
        for ind, shape in enumerate(self.volumetric_examples):
            self.assertEqual(shape.volume(), res[ind],
                             f'''{shape._title} should be {res[ind]},
                             got {shape.volume()}''')

    def test_area(self):
        """ Check area of every volumetric shape"""
        res = [1256.6370614359173, 150, 148, 1.8862680691608995,
               150.79644737231007, 449.5881427866065]
        for ind, shape in enumerate(self.volumetric_examples):
            self.assertEqual(shape.area(), res[ind],
                             f'''{shape._title} should be {res[ind]},
                             got {shape.volume()}''')

    def test_sphere_diameter(self):
        """ Check sphere diameter """
        res = 20
        shape = self.sphere
        self.assertEqual(shape.diameter(), res,
                         f'''{shape._title} should be {res},
                         got {shape.diameter()}''')

    def test_diagonale(self):
        """ Check cube and parallelepiped diagonale """
        res = [8.660254037844386, 8.774964387392123]
        shapes = [self.cube, self.parallelepiped]
        for ind, shape in enumerate(shapes):
            self.assertEqual(shape.diagonal(), res[ind],
                             f'''{shape._title} should be {res[ind]},
                             got {shape.diagonal()}''')

    def test_apothem(self):
        """ Check apothem of the pytramid """
        res = 1.8862680691608995
        shape = self.pyramid
        self.assertEqual(shape.apothem, res,
                         f'''{shape._title} should be {res},
                         got {shape.apothem}''')

    def test_area_side_cylinder(self):
        """ Check side area of the cylinder"""
        res = 94.24777960769379
        shape = self.cylinder
        self.assertEqual(shape.area(True), res,
                         f'''{shape._title} should be {res},
                         got {shape.area(True)}''')


if __name__ == '__main__':
    unittest.main()
