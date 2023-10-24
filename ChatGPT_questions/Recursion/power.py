# Write a Python function to calculate the result of raising a number x to the power of n.

def power(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n < 0:
        return 1/x * power(x, n + 1)
    else:
        return x * power(x, n-1)


print(power(3, -3))

# assert power(2, 3) == 8
# assert power(5, 0) == 1
# assert power(3, -2) == 1/9
