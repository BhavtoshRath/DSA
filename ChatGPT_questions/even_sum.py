# Write a Python function that takes an array of numbers as input and returns the sum of all the even numbers in the array.


def sum_even_numbers(array):
    ans = 0
    for element in array:
        if element % 2 == 0:
            ans += element
    return ans


input_array = [1, 2, 3, 4, 5, 6, 1, 234, 457, 34, 5, 578, 68]
result = sum_even_numbers(input_array)
print(result)
