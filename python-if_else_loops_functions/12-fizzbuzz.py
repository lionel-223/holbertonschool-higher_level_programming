#!/usr/bin/python3
def fizzbuzz():
    multi = ""
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 != 0:
            multi = "Fizz"
            print("{} ".format(multi), end = "")
        elif i % 5 == 0 and i % 3 != 0:
            multi = "Buzz"
            print("{} ".format(multi), end = "")
        elif i % 5 == 0 and i % 3 == 0:
            multi = "FizzBuzz"
            print("{} ".format(multi), end = "")
        else:
            print("{} ".format(i), end = "")
