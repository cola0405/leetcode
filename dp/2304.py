from typing import List
class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[float('inf')]*(m+1) for _ in range(n+1)]
        for i in range(m): 
            dp[0][i] = 0
        for i in range(1,m+1):
            dp[1][i] = grid[0][i-1]
        for i in range(2, n+1):
            for j in range(1, m+1):
                for k in range(1,m+1):
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + moveCost[grid[i-2][k-1]][j-1] + grid[i-1][j-1])
        return min(dp[n])

print(Solution().minPathCost(grid = [[5,1,2],[4,0,3]], moveCost = [[12,10,15],[20,23,8],[21,7,1],[8,1,13],[9,10,25],[5,3,2]]))

