# Sezimgul Zhusupova
# November 2, 2026

# Problem 5: Convert radians to degrees for a user input value, and compare with math.degrees.

import math

radians = float(input("Enter an angle in radians: "))

# Formula: degrees = radians * (180 / pi)
calculated = radians * (180 / math.pi)

print("Calculated degrees:", calculated)
print("math.degrees:", math.degrees(radians))
