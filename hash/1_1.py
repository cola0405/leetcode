from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        idx = {nums[i]:i for i in range(n)}

        for i in range(n):
            x = target-nums[i]
            if x in idx and idx[x] != i:
                return [i, idx[x]]

print(Solution().twoSum(nums = [3,3], target = 6))


