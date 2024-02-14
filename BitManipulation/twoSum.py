# https://leetcode.com/problems/sum-of-two-integers/


def getSum(a: int, b: int) -> int:
    while b != 0:
        carry = (a & b) << 1 # & is "bitwise AND operator". convert a and b to binary and multiply
        a = a ^ b
        b = carry
    return a


a = getSum(4, 2)
print(a)

# 0 1 - 1  a ^ b (xor)
# 1 0 - 1  a ^ b (xor)
# 0 0 - 0  a ^ b (xor)

# 1 1 - 0  a & b (carry 1)  --- (a & b) << 1