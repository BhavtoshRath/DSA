# Question: (revisit)
# Write a recursive function count_even_digits(n) that counts the number of even digits in a positive integer n.


# HINT: [An imp concept] If need to separate out digits in number, use (% 10), (// 10)
# A non-recursive solution
def count_even_digits1(n):
    cntr = 0
    while n != 0:
        m = n % 10
        if m & 2 == 0:
            cntr += 1
        n = n // 10
    return cntr


# print(count_even_digits1(3478568887))

# Doubt: Can recursion have a while loop?
# Base case: single digit
cntr = 0
def count_even_digits2(n):
    last_digit = n % 10
    remaining_digit = n // 10
    if n < 10:
        if n % 2 == 0:
            return 1
        else:
            return 0
    else:
        return (last_digit % 2 == 0) + count_even_digits2(remaining_digit)  # imp way to assign "counter in recursion"


# how does (last_digit % 2 == 0), a boolean serve as counter?

print(count_even_digits2(349885))

