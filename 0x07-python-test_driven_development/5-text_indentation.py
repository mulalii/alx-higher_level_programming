#!/usr/bin/python3
"""
5-text_indentation.py
This module supplies one function, text_indentation(text)
"""



def text_indentation(text):
    """Method for adding 2 new lines after .?: chars
    Args:
        text: The str text.
    Raises:
        TypeError: If text is not a str.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for symb in ".:?":
        text = (symb + "\n\n"). join(
            [line.strip(" ") for line in text.split(symb)])
        print(text, end="")
