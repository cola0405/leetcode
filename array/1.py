from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = dict()

        for i in range(len(nums)):
            x = target-nums[i]
            if x in idx:
                return [i, idx[x]]
            idx[x] = i