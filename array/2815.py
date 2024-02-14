from typing import List
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans = -1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if max(str(nums[i])) == max(str(nums[j])):
                    ans = max(ans, nums[i]+nums[j])
        return ans