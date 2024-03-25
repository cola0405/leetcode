from typing import List
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        already = [[0]*n for _ in range(m)]
        valid = {0:['start'],1:['left', 'right'], 2:['up','down'],
                 3:['right','up'],4:['up','left'],
                 5:['right','down'], 6:['down','left']}
        def dfs(i,j,direction):
            if i < 0 or i >= m or j < 0 or j >= n or already[i][j]:
                return 0
            # check valid previous cell
            if direction != 'start' and direction not in valid[grid[i][j]]:
                return 0
            if i == m-1 and j == n-1:
                return 1
            already[i][j] = 1
            if grid[i][j] == 1:
                return dfs(i,j+1,'right') + dfs(i,j-1,'left')
            elif grid[i][j] == 2:
                return dfs(i+1,j,'down') + dfs(i-1,j,'up')
            elif grid[i][j] == 3:
                return dfs(i,j-1,'left') + dfs(i+1,j,'down')
            elif grid[i][j] == 4:
                return dfs(i+1,j,'down') + dfs(i,j+1,'right')
            elif grid[i][j] == 5:
                return dfs(i-1, j,'up')+dfs(i, j-1,'left')
            elif grid[i][j] == 6:
                return dfs(i-1, j,'up')+dfs(i, j+1,'right')
        return dfs(0,0,'start') == 1

print(Solution().hasValidPath([[4,1,3],[6,1,2]]))