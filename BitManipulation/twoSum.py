# https://leetcode.com/problems/sum-of-two-integers/


def getSum(a: int, b: int) -> int:
    while b != 0:
        tmp = (a & b) << 1
        a = a ^ b
        b = tmp
    return a



a = getSum(4, 0)
print(a)