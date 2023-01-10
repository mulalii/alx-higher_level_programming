#!/usr/bin/python3
"""Module for class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """new instance of Rectangle
        Args:
            width: width of a rectangle
            height: height of a rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Implementation of area method"""
        return self.__width * self.__height

    def __str__(self):
        """Implementation of area method"""
        return "[{}] {:d}/{:d}".format(Rectangle.__name__, self.__width,
                                       self.__height)
