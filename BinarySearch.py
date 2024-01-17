# Given an array of integers arr which is sorted in ascending order,
# and an integer target, write a function to search target in arr.
# If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.
# Assume array is sorted

def binary_search(arr, target):  # O(Log N)
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high)//2
        mid_val = arr[mid]
        if mid_val == target:
            return mid
        if mid_val < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example usage:
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_value = 7
result = binary_search(sorted_array, target_value)
print(result)