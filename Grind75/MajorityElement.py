# https://leetcode.com/problems/majority-element/description/


def majorityElement1(nums):  # Time C O(N), Space: O(N)
    maj_dict = {}
    for num in nums:
        if num in maj_dict:
            maj_dict[num] += 1
        else:
            maj_dict[num] = 1
    return max(maj_dict, key=maj_dict.get)


print(majorityElement1([1, 2, 3, 4, 3, 3, 2, 3]))


def majorityElement2(nums):  # Time C O(N), Space: O(N) [Boyer-Moore Voting Algorithm]
    # Works only when majority element exists alteast n/2 times.
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
