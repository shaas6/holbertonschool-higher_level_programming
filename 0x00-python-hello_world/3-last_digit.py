#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_string = str(number)
z = number_string[-1]
x = int(z)
if number < 0:
    x = x * -1
if x > 5:
    print("Last digit of", number, "is", x, "and is greater than 5")
if x == 0:
    print("Last digit of", number, "is", x, "and is 0")
if x < 6 and x != 0:
    print("Last digit of", number, "is", x, "and is less than 6 and not 0")
