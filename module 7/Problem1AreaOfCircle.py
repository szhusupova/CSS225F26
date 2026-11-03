# Sezimgul
# 2026-11-03
# Problem 1: Area of a circle using the math module

import math


def areaOfCircle(r):
    # Return the area of a circle with radius r
    return math.pi * r ** 2


# Test the function with a sample radius
radius = 5
print("Radius:", radius)
print("Area:", areaOfCircle(radius))
