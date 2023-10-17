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


# Using memoization
# Time: O(n)
memoize = []
memoize.append(0)
memoize.append(1)
def getNthFib2(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if len(memoize) <= n:
        return memoize[n]
    else:
        memoize[n] = getNthFib2(n - 1) + getNthFib2(n - 2)
        return memoize[n]


print(getNthFib2(5))