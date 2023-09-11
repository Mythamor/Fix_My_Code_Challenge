#!/usr/bin/python3
"""
Class Square Module that defines width and height
"""

class Square():
    """
    Attr:
        width
        height
    Methods:
        __init__
        area_of_my_square(self)
        PerimeterOfMySquare(self)
        __str__(self)
    """


    def __init__(self, width=0, height=0):
        """Initialize square instance with width and height"""
        self._width = width
        self._height = height

    @property
    def width(self):
        """ Width getter attribute """
        return self._width

    @width.setter
    def width(self, value):
        """ Width setter attribute """
        if value > 0:
            self._width = value
        else:
            raise ValueError("Width must be a positive")

    @property
    def height(self):
        """ Height getter attribute """
        return self._height

    @height.setter
    def height(self, value):
        """ Height setter atttribute """
        if value > 0:
            self._height = value
        else:
            raise ValueError("Height must be positive")

    def area_of_my_square(self):
        """ Area of the square """
        return self._width * self._height

    def PermiterOfMySquare(self):
        return (self._width * 2) + (self._height * 2)

    def __str__(self):
        return "{}/{}".format(self._width, self._height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
