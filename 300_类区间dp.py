from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [1]*n  # dp[i]表示以nums[i]结尾的最长子序列,初始化值为1

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:   # 根据更新条件来写循环
                    dp[i] = max(dp[j]+1, dp[i])

        return max(dp)

Solution().lengthOfLIS([1,3,6,7,9,4,10,5,6])

