from typing import List
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        ans = float('inf')
        for i in range(1, len(nums)-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                ans = min(ans, nums[i]+nums[i-1]+nums[i+1])
        return ans if ans != float('inf') else -1