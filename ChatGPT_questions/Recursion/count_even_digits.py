# Question:
# Write a recursive function count_even_digits(n) that counts the number of even digits in a positive integer n.


# HINT: If need to separate out digits in number, use (% 10), (// 10)
def count_even_digits(n):
    m = n % 10
    if m & 2 == 0:
        cntr = 1
    new_n = n // 10
    count_even_digits(new_n)
    print(m, new_n)


count_even_digits(346)