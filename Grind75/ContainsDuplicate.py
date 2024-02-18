# https://leetcode.com/problems/contains-duplicate/description/


# sol 1: Two for loops : Space complexity O(1);  time complexity: O(n^2)
# sol 2: Sort and check for equal adj items: Space complexity O(1);  time complexity: O(n + nlogn)
def contains_duplicate(nums):  # Space and time complexity: O(n)
    d = {}
    for num in nums:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
    if max(d.values()) > 1:
        return True
    else:
        return False
