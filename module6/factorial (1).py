# Sezimgul Zhusupova
# November 2, 2026

# Problem 6: Use a for statement to calculate the factorial of a user input value, and compare with math.factorial.

import math

n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # n! = 1 * 2 * 3 * ... * n  (0! is 1, since the loop never runs)
    result = 1
    for i in range(2, n + 1):
        result *= i

    print("Calculated factorial:", result)
    print("math.factorial:", math.factorial(n))
