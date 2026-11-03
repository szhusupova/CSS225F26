# Sezimgul
# 2026-11-03
# Problem 2: Check whether a number is in a given range


def checkRange(n):
    # Print whether n is inside range(1, 10)
    if n in range(1, 10):
        print(n, "is in the range.")
    else:
        print(n, "is not in the range.")


# Test the function with a number inside and one outside the range
checkRange(5)
checkRange(15)
