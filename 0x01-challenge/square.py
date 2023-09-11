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
        __init__(self, *args, **kwargs)
        area_of_my_square(self)
        PerimeterOfMySquare(self)
        __str__(self)
    """


    def __init__(self, width=0, height =0):
        """Initialize square instance with width and height"""
        self.width = width
        self.height = height

        if self.height != self.width:
            self.height = self.width
        if self.width != self.height:
            self.width = self.height

    @property
    def width(self):
        """ Getter returns width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter sets width if int > 0 """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter returns height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter sets height if int > 0 """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


    def area_of_my_square(self):
        """ Area of the square """
        return self.__width * self.__height

    def PermiterOfMySquare(self):
        """ Perimeter of the square """
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ String representation of the class"""
        return "{}/{}".format(self.__width, self.__height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
