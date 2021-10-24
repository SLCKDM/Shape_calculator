import shapes as sh


class AdventureDone(Exception):
    """ Excerption that let us close program """
    pass


class Main():
    """ This class represents user interface

    Methods:
        shape_ind_choice(): select the shape_ind to be calculated from
        operation_choice(): choose operation that will be calculated
        attributes_input(): initial values, which will be used in calculations
        process() : makes logic

    Raises:
        AdventureDone: if user input contains "close" - terminate process
    """

    shape_inds = [sh.Circle, sh.Square, sh.Rhombus,
                  sh.Rectangle, sh.Trapezoid, sh.Triangle,
                  sh.Sphere, sh.Cube, sh.Parallelepiped,
                  sh.Pyramid, sh.Cylinder, sh.Cone]

    attr_dict = {
        'Circle': 'radius',
        'Square': 'side',
        'Rhombus': 'side, height',
        'Rectangle': '2 sides',
        'Trapezoid': '4 sides and height',
        'Triangle': '3 sides',
        'Sphere': 'radius',
        'Cube': 'side',
        'Parallelepiped': '3 sides',
        'Pyramid': 'edge, radius, sides',
        'Cylinder': 'radius, height',
        'Cone': 'radius, height'
    }

    def shape_ind_choice(self):
        """ return index of shape_ind class """
        for ind, shape_ind in enumerate(self.shape_inds):
            print(f'\n{ind}. {shape_ind._title}', end='')
        shape_ind_input = input(
            "\nWhich figure you want to calculate ('close' to exit)?\n")
        if shape_ind_input == "close":
            raise AdventureDone
        else:
            return int(shape_ind_input)

    def operation_choice(self, shape_ind: int):
        """ return string of code that will be executed
        shape_ind: ind
        """
        method_list = [method for method in dir(
            self.shape_inds[shape_ind])
            if method.startswith('__' and '_') is False]
        for ind, method in enumerate(method_list):
            print(f'\n{ind}. {method}', end='')
        operation_input = input(
            f'\nWhich operation you want to calculate to \
            {self.shape_inds[shape_ind]._title.lower()}?\n')
        if operation_input == "close":
            raise AdventureDone
        else:
            return f'sh.{self.shape_inds[shape_ind].__name__} \
                    {self.attributes_input(shape_ind)}.    \
                    {method_list[int(operation_input)]}()'

    def attributes_input(self, shape_ind: int):
        """ asks the user to enter values that
        will be used as attributes in shape class.
        Return attributes tuple
        """
        print(
            f"Enter the following values ​​with spaces in between:  \
            {self.attr_dict[self.shape_inds[shape_ind].__name__]}")
        attr_input = input('(Example: X Y Z): ')
        if attr_input.strip() == "close":
            raise AdventureDone
        return tuple(map(int, attr_input.split(' ')))

    def process(self):
        """ make stupid, but logic of this programm
        First, it asks to enter which figure the user is interested in
        Secondly, it asks you to enter the operation that needs to be performed
        Thirdly, it asks you to enter the initial data for the calculation
        And then the user gets the result.
        Any time user can enter 'close' in input and process will be terminated
        Also, if user enters something incorrectly, programm tells about it and
        it does not give a result
        """
        while True:
            try:
                shape_ind = self.shape_ind_choice()
                operation = self.operation_choice(shape_ind)
                print(eval(operation))
            except IndexError:
                print("Seems you entered something wrong, try again")
            except AdventureDone:
                break


if __name__ == "__main__":
    pass
