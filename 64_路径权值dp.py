from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid[0]), len(grid)
        # dp[i][j] 表示当前位置的最小权值
        dp = [[0] * n for _ in range(m)]

        # dp init
        dp[0][0] = grid[0][0]
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for j in range(1,m):
            dp[j][0] = dp[j-1][0] + grid[j][0]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[-1][-1]

print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))