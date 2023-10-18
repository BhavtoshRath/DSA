# Time: O(2^n) -> lot of duplicate computations
# Space: O(n) -> Nothing is being stored, bt we do use call stack. 1 storage unit for each of n.
def getNthFib1(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return getNthFib1(n - 1) + getNthFib1(n - 2)

# print(getNthFib1(10))


# Using memoization (used to optimize recursive algorithms by storing the results
# of expensive function calls and reusing them when the same inputs occur again)
# Time: O(n)
fib_cache = {}
fib_cache[1] = 0
fib_cache[2] = 1
def getNthFib2(n):
    if n in fib_cache:
        return fib_cache[n]
    else:
        fib_cache[n] = getNthFib2(n - 1) + getNthFib2(n - 2)
        return fib_cache[n]


print(getNthFib2(21))
