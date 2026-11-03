# Sezimgul Zhusupova
# November 2, 2026

# Problem 4: Approximate pi with simple arithmetic and compare it to math.pi.

import math

# Leibniz series: pi/4 = 1 - 1/3 + 1/5 - 1/7 + ...
# More terms gives a better approximation.
terms = 1000000
total = 0
sign = 1
for k in range(terms):
    total += sign / (2 * k + 1)
    sign = -sign

approx_pi = 4 * total

print("Approximation of pi (Leibniz,", terms, "terms):", approx_pi)
print("math.pi:", math.pi)
