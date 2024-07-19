#!/usr/bin/python3
def print_last_digit(number):
    lasD = 0
    if number < 0:
        lastD = (-number % 10)
    else:
        lastD = number % 10
    print(lastD, end='')
    return lastD
