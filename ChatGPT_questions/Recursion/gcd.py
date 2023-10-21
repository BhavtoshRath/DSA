# Write a recursive function to find the greatest common divisor (GCD)
# of two positive integers, 'a' and 'b', using the Euclidean algorithm.
# The GCD of two integers is the largest positive integer that divides
# both 'a' and 'b' without leaving a remainder.

# ** The Euclidean algorithm involves repeatedly taking the remainder of 'a'   12 18
# divided by 'b' until 'b' becomes zero. The last non-zero remainder is the GCD of 'a' and 'b'. **

# Ex - 270a and 192b
# 270 = 1*192 + 78
# 192 = 2*78 + 36
# 78 = 2*36 + [6]
# 36 = 6*6 + 0


# Non-recursive. Iterative
def gcd1(a, b):
    while b != 0:
        rem = a % b
        a = b
        b = rem
    return abs(a)


# print(gcd(12, 8))
# print(gcd(45, 60))
# print(gcd(45, -60))  # When calculating the GCD, it is common practice to use the absolute values of the numbers,
# print(gcd(123456789, 987654321))
# print(gcd(-12, -18))


def gcd2(a, b):
    rem = a % b
    if rem == 0:
        return abs(b)
    else:
        return gcd2(b, rem)


# print(gcd2(12, 8))
# print(gcd2(45, 60))
# print(gcd2(270, 192))
# print(gcd2(123456789, 987654321))
