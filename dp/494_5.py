# 同之前的2000dp
# 但是dp构造为
# -1000, -999, ..., -2, -1, 0, 1, 2, 3
# 省去了很多边界的判断

from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[0]*2001 for _ in range(2)]
        # 前i个数，和为j的方法数
        dp[0][1000] = 1
        last = 0
        cur = 1
        for i in range(n):
            for j in range(2001):
                dp[cur][j] = 0
                if j-nums[i] >= 0:
                    dp[cur][j] += dp[last][j-nums[i]]
                if j+nums[i] < 2000:
                    dp[cur][j] += dp[last][j+nums[i]]
            cur, last = last, cur

        if target >= 0:
            return dp[last][target+1000]
        else:
            return dp[last][1000+target]

print(Solution().findTargetSumWays(nums = [9,7,0,3,9,8,6,5,7,6], target = 2))