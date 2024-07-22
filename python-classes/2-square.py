#!/usr/bin/python3
"""A Square class for practicing object-oriented programming."""

class Square:
    """This is a Square class that defines a square."""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size