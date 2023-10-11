# You are given an integer n, where n represents the number of steps in a staircase.
# You can climb the staircase either by taking one step or two steps at a time.
# Write a Python function to find the total number of distinct ways to climb the staircase.

from icecream import ic

def climb_stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    ic(climb_stairs(n - 1) + climb_stairs(n - 2))
    return climb_stairs(n-1) + climb_stairs(n-2)

# 1: 1 (1)
# 2: 1+1,2 (2)
# 3: 1+1+1, 1+2, 2+1 (3) 2+1
# 4: 1+1+1+1, 1+2+1, 1+1+2, 2+1+1, 2+2 (5) 3+2
# 5: 1+1+1+1+1, 1+2+2, 2+2+1, 2+1+2, 1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1 (8) 5+3
#6: 1+1+1+1+1+1, 2+2+2, 1+1+1+1+2, 1+1+1+2+1, 1+1+2+1+1, 1+2+1+1+1, 2+1+1+1+1
    # 1+1+2+2, 1+2+1+2, 2+1+1+2, 2+1+2+1, 2+2+1+1, 1+2+2+1 (13) 8+5

# N = 6

climb_stairs(5)