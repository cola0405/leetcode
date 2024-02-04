from typing import List
class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
               total = grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1]
               total += grid[i][j]
               total += grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1]
               ans = max(ans, total)
        return ans