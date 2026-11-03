# Sezimgul
# 2026-11-03
# Problem 4: Return a new list with the unique elements of a list


def uniqueElements(numbers):
    # Build a new list containing each number only once
    unique = []
    for num in numbers:
        if num not in unique:
            unique.append(num)
    return unique


# Test the function with the given list
sample = [1, 3, 3, 3, 6, 2, 3, 5]
print("Original list:", sample)
print("Unique elements:", uniqueElements(sample))
