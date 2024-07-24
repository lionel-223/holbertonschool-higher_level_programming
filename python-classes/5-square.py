#!/usr/bin/python3
"""A Square class for practicing object-oriented programming."""


class Square:
    """This is a Square class that defines a square."""
    def __init__(self, size=0):
        """Initializes the square with a given size."""
        self.size = size  # Utilise le setter pour la validation

    @property
    def size(self):
        """Getter method to retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Method to calculate and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Method that prints in stdout the square with the character #"""
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                print("#" * self.size)
        return
