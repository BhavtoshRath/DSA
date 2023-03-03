from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    l = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                l.append(i)
                l.append(j)
    return l


ans = twoSum([2,7,11,15], 9)
ans = twoSum([3,2,4], 6)
ans = twoSum([3,3], 6)
print(ans)