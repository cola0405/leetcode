# 用了记录，但是O(n2) 超时
# 2是最优解 O(n)

from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')]*n
        dp[0] = 0
        for i in range(1, n):
            for j in range(0,i):
                if nums[j] >= i-j:
                    dp[i] = min(dp[j]+1, dp[i])
        return dp[-1]
print(Solution().jump([2,3,0,1,4]))