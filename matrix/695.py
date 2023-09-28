from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def search_land(row, column):
            if ((row<0 or row>=m) or (column<0 or column>=n)
                    or visit[row][column] or grid[row][column]==0):
                return 0

            visit[row][column] = 1
            return (1 + search_land(row+1, column) + search_land(row-1, column)
                    + search_land(row,column+1) + search_land(row, column-1))

        m = len(grid)
        n = len(grid[0])
        visit = [[0]*n for _ in range(m)]

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(search_land(i,j), ans)
        return ans

    