from typing import List
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0]*501 for _ in range(n)]        # 到第 i为等差值为 j的等差数列的最大长度
        for i in range(1, n):
            for k in range(501):
                dp[i][k] = dp[i-1][k]
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = dp[i-1][diff] + 1
        return max(dp[-1]) + 1

print(Solution().longestArithSeqLength([83,20,17,43,52,78,68,45]))