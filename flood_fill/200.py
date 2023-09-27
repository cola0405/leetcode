from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def mark_land(row, column):
            if (row<0 or row>=m) or (column<0 or column>=n)\
                or grid[row][column] == '0':
                return
            grid[row][column] = '0'
            mark_land(row+1, column)
            mark_land(row-1, column)
            mark_land(row, column+1)
            mark_land(row, column-1)

        ans = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    mark_land(i, j)
                    ans += 1
        return ans
