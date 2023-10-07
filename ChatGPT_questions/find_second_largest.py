# Write a Python function that takes an array of integers as input and
# returns the second largest element in the array.
# If there is no second largest element, return None.

def find_second_largest(input_array):
    seq = sorted(list(set(input_array))[-2:])
    if len(seq) != 2:
        return None
    else:
        return seq[0]


# Test cases
print(find_second_largest([1, 2, 3, 4, 5]))  # Should output 4
print(find_second_largest([7, 7, 7, 7]))  # Should output None
print(find_second_largest([5, 2, 9, 8, 1, 3, 6]))  # Should output 8
print(find_second_largest([10, 10, 10, 10, 10]))  # Should output None
print(find_second_largest([5, 10, 8, 3, 2, 9]))  # Should output 9