# Write a recursive function to find the greatest common divisor (GCD)
# of two positive integers, 'a' and 'b', using the Euclidean algorithm.
# The GCD of two integers is the largest positive integer that divides
# both 'a' and 'b' without leaving a remainder.

# ** The Euclidean algorithm involves repeatedly taking the remainder of 'a'   12 18
# divided by 'b' until 'b' becomes zero. The last non-zero remainder is the GCD of 'a' and 'b'. **

# Non-recursive. Iterative
def gcd(a, b):
    while b != 0:
        rem = a % b
        a = b
        b = rem
    return abs(a)


print(gcd(12, 8))
print(gcd(45, 60))
print(gcd(45, -60))  # When calculating the GCD, it is common practice to use the absolute values of the numbers,
print(gcd(123456789, 987654321))
print(gcd(-12, -18))
