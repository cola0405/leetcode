from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[0]*2001 for _ in range(n+1)]
        # 前i个数，和为j的方法数
        dp[0][0] = 1

        for i in range(1, n+1):
            for j in range(2001):
                if j <= 1000:
                    # +nums[i]
                    if j-nums[i-1] >= 0:
                        dp[i][j] += dp[i-1][j-nums[i-1]]
                    else:
                        dp[i][j] += dp[i-1][-(j-nums[i-1])+1000]

                    # -nums[
                    if j+nums[i-1] <= 1000:
                        dp[i][j] += dp[i-1][j+nums[i-1]]
                else:
                    if j+nums[i-1] <= 2000:
                        dp[i][j] += dp[i-1][j+nums[i-1]]
                    dp[i][j] += dp[i-1][-(j-1000-nums[i-1])]
        if target >= 0:
            return dp[n][target]
        else:
            return dp[n][-target+1000]

print(Solution().findTargetSumWays(nums = [9,7,0,3,9,8,6,5,7,6], target = 2))