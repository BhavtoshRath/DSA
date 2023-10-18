# Question:
# Write a recursive function sum_numbers(n) that calculates the sum of all positive integers from 1 to n.

def sum_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_numbers(n-1)

for i in range(1, 10):
    print(sum_numbers(i))

# 1,3,6,10,15,21,28,36,45,55....