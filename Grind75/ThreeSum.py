# https://leetcode.com/problems/3sum/description/
# https://www.youtube.com/watch?v=jzZsG8n2R9A&ab_channel=NeetCode


def threeSum(nums):
    nums.sort()  # O(NlogN)
    result = []

    for i, a in enumerate(nums): # O(N^2)
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l_ptr, r_ptr = i + 1, len(nums) - 1
        while l_ptr < r_ptr:
            if nums[i] + nums[l_ptr] + nums[r_ptr] > 0:
                r_ptr -= 1
            elif nums[i] + nums[l_ptr] + nums[r_ptr] < 0:
                l_ptr += 1
            else:
                result.append([nums[i], nums[l_ptr], nums[r_ptr]])
                l_ptr += 1   ###
                while nums[l_ptr] == nums[l_ptr - 1] and l_ptr < r_ptr:  ###
                    l_ptr += 1  ###
    return result


# Lines 20-22 are difficult to understand