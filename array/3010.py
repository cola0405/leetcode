from typing import List
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        ans = float('inf')
        for j in range(1, len(nums)):
            for k in range(j+1, len(nums)):
                ans = min(ans, nums[j]+nums[k])
        return ans + nums[0]