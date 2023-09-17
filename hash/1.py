from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = dict()
        for i in range(len(nums)):
            num = target-nums[i]
            if num in idx:
                return [i, idx[num]]
            idx[nums[i]] = i

print(Solution().twoSum(nums = [3,3], target = 6))


