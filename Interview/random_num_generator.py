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
        temp1 = 1
        temp2 = 0
        while temp1 < k:
            temp2 += rand_n() * N
            temp1 *= N
        return temp2
        # return result + result % k


print(rand_k(4))
print(rand_k(5))
print(rand_k(1000))
# for i in range(0, 1000):
#     print(i, rand_k(1000))
#     i += 1