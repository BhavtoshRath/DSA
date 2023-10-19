# Question:
# Write a recursive function to reverse a positive integer 'n'.
# For example, if 'n = 12345', the reversed number should be '54321'.
# Write a recursive function reverse_number(n) to reverse the digits in 'n'.

def reverse_number(n):
    last_digit = n % 10
    remaining_digits = n // 10
    if remaining_digits == 0:
        return last_digit
    else:
        return int(str(last_digit) + str(reverse_number(remaining_digits)))


print(reverse_number(122453), type(reverse_number(122453)))