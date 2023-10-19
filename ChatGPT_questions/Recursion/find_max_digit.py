# Question:
# Write a recursive function to find the maximum digit in a positive integer 'n'.
# For example, for 'n = 738912', the maximum digit is 9.
# Write a recursive function find_max_digit(n) to calculate the maximum digit in 'n'.


def find_max_digit(n):
    last_digit = n % 10
    remaining_digits = n // 10
    if remaining_digits == 0:
        return last_digit
    else:
        return max(last_digit, find_max_digit(remaining_digits))

print(find_max_digit(814273))