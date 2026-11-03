# Sezimgul Zhusupova
# November 2, 2026

# Problem 1: Use a for statement and random.randrange to print 10 random integers between 25 and 35.

import random

# randrange(start, stop) excludes stop, so use 36 to include 35
for i in range(10):
    print(random.randrange(25, 36))
