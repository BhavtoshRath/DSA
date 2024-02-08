# https://leetcode.com/problems/majority-element/description/

def majorityElement(nums):  # Time C O(N), Space: O(N)
    maj_dict = {}
    for num in nums:
        if num in maj_dict:
            maj_dict[num] += 1
        else:
            maj_dict[num] = 1
    return max(maj_dict, key=maj_dict.get)

print(majorityElement([1,2,3,4,3,3,2,3]))
