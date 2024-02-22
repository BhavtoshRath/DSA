# Given an array of integers nums and an integer targetSum,
# return indices of the two numbers such that they add up to targetSum.


def twoNumberSum1(array, targetSum):  # Approach 1: brute force (O(N^2))
    l = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == targetSum:
                l.append(i)
                l.append(j)
    return l


def twoNumberSum2(array, targetSum):  # Approach 2: Hash map/dict (O(N))
    d = {}
    for index, value in enumerate(array):
        d[value] = index
        key_set = set(d.keys())
        if targetSum - value in key_set and targetSum != 2 * value:
            return [value, targetSum - value]
    else:
        return []


def twoNumberSum3(array, targetSum):  # Approach 3: Sort, and then using pointers (O(N))
    sorted_array = sorted(array)
    left_ptr = 0
    right_ptr = len(sorted_array) - 1
    while left_ptr < right_ptr:
        if sorted_array[left_ptr] + sorted_array[right_ptr] == targetSum:
            return [sorted_array[left_ptr], sorted_array[right_ptr]]
        if sorted_array[left_ptr] + sorted_array[right_ptr] < targetSum:
            left_ptr += 1
        elif sorted_array[left_ptr] + sorted_array[right_ptr] > targetSum:
            right_ptr -= 1
    return []


def twoSum1(nums, target): # (In leetcode grind75) soln: returning indices
    d = {}
    for index in range(len(nums)):
        if nums[index] not in d:
            d[nums[index]] = index
        if (target - nums[index]) in d:
            if index != nums.index(target - nums[index]):
                return [index, nums.index(target - nums[index])]


def twoSum2(nums, target):  # soln: returning the numbers
    s = set()
    for num in nums:
        if target - num in s:
            return [num, target-num]
        else:
            s.add(num)

def twoSum3(nums, target):
    d = {}
    for i in range(len(nums)):
        d[nums[i]] = i
        val = list(d.keys())
        if target - nums[i] in val:
            return [d[nums[i]], d[target - nums[i]]]
array = [2,7,11,15]
targetSum = 9
x = twoSum3(array, targetSum)
print(x)
