class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1,1,2]
        for i in range(n-2):
            dp[0] = dp[1]
            dp[1] = dp[2]
            dp[2] = dp[0] + dp[1]

        return dp[-1]
