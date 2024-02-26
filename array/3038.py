from typing import List
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        i = 0
        ans = 0
        target = nums[0]+nums[1]
        while i+1 < len(nums) and nums[i]+nums[i+1] == target:
            ans += 1
            i += 2
        return ans

