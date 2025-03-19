# 01背包问题 每个只取一次
# dp[i]取决于dp[i - j**x]
# 每次dp只取决于上一个状态
# 所以可以从右往左dp

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(1,n+1):
            for j in range(n+1)[::-1]:
                k = j - i**x
                if k < 0: break
                dp[j] = int((dp[j] + dp[k]) % (1e9+7))
        return dp[n]

print(Solution().numberOfWays(n = 213, x = 1))