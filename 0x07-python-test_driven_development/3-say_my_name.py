#!/usr/bin/python3
"""
3-say_my_name.py module
3-say_my_name.py module supplies one function: say_my_name
"""


def say_my_name(first_name, last_name=""):
    """Function that prints first and last name
    
    Args:
        first_name: string
        last_name: string
    Raises:
        TypeError: if first_name or last_name are not strings
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
