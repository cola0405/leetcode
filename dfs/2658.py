from typing import List
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or already[i][j]:
                return 0
            already[i][j] = 1
            return grid[i][j] + dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1)

        m = len(grid)
        n = len(grid[0])
        already = [[0]*n for _ in range(m)]
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    ans = max(ans, dfs(r,c))
        return ans

print(Solution().findMaxFish([[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]))