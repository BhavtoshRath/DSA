def isValidSubsequence1(array, sequence):
    for item in array:
        if item == sequence[0]:
            sequence.pop(0)
        if len(sequence) == 0:
            return True
    else:
        return False


def isValidSubsequence2(array, sequence):
    if len(array) < len(sequence):
        return False
    ptr = 0
    for item in array:
        if item in sequence[ptr:]:
            ptr += 1
    if len(sequence) == ptr:
        return True
    else:
        return False

def isValidSubsequence3(array, sequence):
    arr_ptr = 0
    seq_ptr = 0
    while arr_ptr < len(array):
        if array[arr_ptr] == sequence[seq_ptr]:
            arr_ptr += 1
            seq_ptr += 1
        else:
            arr_ptr += 1
        if seq_ptr == len(sequence):
            return True
    return False


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

x = isValidSubsequence(array, sequence)
print(x)