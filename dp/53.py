from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('-inf')
        dp = [float('-inf')]*(n+1)
        for i in range(1, n+1):
            dp[i] = max(dp[i-1]+nums[i-1], nums[i-1])       # nums[i]取或不取两种情况（-1是offset）
            ans = max(dp[i], ans)
        return ans
