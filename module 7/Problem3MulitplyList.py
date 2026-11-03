# Sezimgul
# 2026-11-03
# Problem 3: Multiply all the numbers in a list


def multiplyList(numbers):
    # Return the product of every number in the list
    total = 1
    for num in numbers:
        total = total * num
    return total


# Test the function with the given list
sample = [5, 2, 7, -1]
print("List:", sample)
print("Product:", multiplyList(sample))
