# dfs + check order
from typing import List
class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        def dfs(i, j, last):
            if i < 0 or i >= m or j < 0 or j >= n:
                grid[last[0]][last[1]] = color
                return
            if already[i][j]:       # don't need to color the last when meet with already
                return
            if grid[i][j] != origin:    # it's not already, and it's different from the origin
                grid[last[0]][last[1]] = color
                return
            already[i][j] = 1
            dfs(i+1,j,(i,j))
            dfs(i-1,j,(i,j))
            dfs(i,j+1,(i,j))
            dfs(i,j-1,(i,j))

        m = len(grid)
        n = len(grid[0])
        already = [[0]*n for _ in range(m)]
        origin = grid[row][col]
        dfs(row, col,(row,col))
        return grid

print(Solution().colorBorder([[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2))