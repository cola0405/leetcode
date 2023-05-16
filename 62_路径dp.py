class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j] 表示路径数
        dp = [[0]*n for _ in range(m)]

        # dp init
        for i in range(n):
            dp[0][i] = 1
        for j in range(m):
            dp[j][0] = 1

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]

print(Solution().uniquePaths(m = 3, n = 7))
