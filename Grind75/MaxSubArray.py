# https://leetcode.com/problems/maximum-subarray/description/
# for similar problems: https://zerobone.net/blog/cs/kadane-algorithm/
def max_subarray(nums):
    max_sum = nums[0]
    curr_sum = nums[0]
    for num in nums[1:]:
        max_sum = max(num, num + max_sum)
        curr_sum = max(curr_sum, max_sum)
        print(num, max_sum, curr_sum)

    return max_sum

nums = [-2, 1, -3, 4, -1, 2, 1, -5, -2, 5]
print("Maximum sum of contiguous subarray:", max_subarray(nums))

