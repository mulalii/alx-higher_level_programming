#!/usr/bin/python3
"""Module for class BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry"""
    def __init__(self):
        """new instance of BaseGeometry"""
        pass

    def area(self):
        """Public instance method that raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method to validate value is an int"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
