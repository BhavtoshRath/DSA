def sortedSquaredArray(array):
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


sol1 = sortedSquaredArray([1, 3, 2, 4])
sol2 = sortedSquaredArray([-3, -2, 1, 4])

print(sol1, sol2)
