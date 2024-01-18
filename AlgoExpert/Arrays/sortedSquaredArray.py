# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.


def sortedSquaredArray1(array): # brute force. O(N + NlogN) ~ O(NlogN) Time complexity of sorting algo
    sol = [i**2 for i in array] # O(N)
    return sorted(sol) # O(NlogN)

def sortedSquaredArray2(array):  # Using pointers O(N)
    sol = [0 for _ in array]
    left_ptr = 0
    right_ptr = len(array) - 1
    for idx in reversed(range(len(array))):
        if abs(array[left_ptr]) > abs(array[right_ptr]):
            sol[idx] = array[left_ptr] ** 2
            left_ptr += 1
        else:
            sol[idx] = array[right_ptr] ** 2
            right_ptr -= 1
    return sol

sol1 = sortedSquaredArray2([1, 3, 2, 4])
sol2 = sortedSquaredArray2([-3, -2, 1, 4])

print(sol1, sol2)
