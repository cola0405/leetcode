# n - 最长递增子序列长度即可
from typing import List
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        for i in range(1,n):        # 这里不能做dp[i] = dp[i-1] 因为dp[i]表示确定以nums[i]结尾的序列
            for j in range(i):
                if nums[i] >= nums[j]:      # 往前找可以接上的子序列
                    dp[i] = max(dp[i],dp[j]+1)
        return n - max(dp)

print(Solution().minimumOperations([3,1,2]))