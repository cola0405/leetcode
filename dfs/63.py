from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def dfs(row, column):
            if row<0 or row>=n or column<0 or column>=m \
                    or obstacleGrid[row][column]==1 or record[row][column]==0:
                return 0

            if row==n-1 and column==m-1:
                return 1
            if record[row][column]>=1:
                return record[row][column]

            record[row][column] = dfs(row+1, column)+dfs(row, column+1)
            return record[row][column]

        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        record = [[-1]*m for _ in range(n)]
        return dfs(0, 0)


print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))