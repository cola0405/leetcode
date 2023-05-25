from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n,m = len(obstacleGrid[0]), len(obstacleGrid)

        # dp[i][j] 表示路径数
        dp = [[0]*n for _ in range(m)]

        # dp init
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1
        for j in range(m):
            if obstacleGrid[j][0] == 1:
                break
            dp[j][0] = 1

        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]

print(Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))