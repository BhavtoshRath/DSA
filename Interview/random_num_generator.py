'''
Random Number Generator
We now have a random number generator that can uniformly generate integers within [0, N).
Please use it to implement another random number generator that can uniformly generate integers within [0, K).
'''

import random

N = 5
def rand_n():
    return random.randint(0, N-1)


def rand_k(k):
    result = rand_n()
    if k == N:
        return result
    if k < N:
        if result >= k:
            return rand_k(k)  # Recursively call rand_k until k < N
        else:
            return result
    else:
        return result % k


print(rand_k(4))
print(rand_k(5))
print(rand_k(7))