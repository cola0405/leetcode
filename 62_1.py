# 压缩dp到两行
# 真抽象。。
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j] 表示路径数
        dp = [[0]*n for _ in range(2)]

        # dp init
        for i in range(n):
            dp[0][i] = 1
        dp[1][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                t = (i-1)%2
                dp[i%2][j] = dp[t][j] + dp[i%2][j-1]

        return dp[(m-1)%2][-1]

print(Solution().uniquePaths(m = 1, n = 2))
