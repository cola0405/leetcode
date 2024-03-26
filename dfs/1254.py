from typing import List
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return -float('inf')
            if already[i][j] or grid[i][j] != 0:
                return 0
            already[i][j] = 1
            return dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1)

        m = len(grid)
        n = len(grid[0])
        already = [[0]*n for _ in range(m)]
        ans = 0
        for a in range(m):
            for b in range(n):
                if grid[a][b] == 0 and already[a][b] == 0 and dfs(a,b) == 0:
                    ans += 1
        return ans

print(Solution().closedIsland([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]))