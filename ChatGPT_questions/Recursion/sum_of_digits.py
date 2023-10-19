# Question:
# Write a recursive function to find the sum of digits in a positive integer 'n'.
# For example, for 'n = 123', the sum of its digits is 1 + 2 + 3 = 6.
# Write a recursive function sum_of_digits(n) to calculate the sum of digits in 'n'.


# Similar idea as count_even_digits
def sum_of_digits(n):
    last_digit = n % 10
    remaining_digits = n // 10
    if remaining_digits == 0:
        return last_digit
    else:
        return last_digit + sum_of_digits(remaining_digits)

print(sum_of_digits(35))