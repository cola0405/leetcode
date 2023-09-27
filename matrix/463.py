# 灵活使用or

from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def get_edges(row, column):
            res = 0
            if row+1 == m or grid[row+1][column] == 0:
                res += 1
            if row-1 < 0 or grid[row-1][column] == 0:
                res += 1
            if column+1 == n or grid[row][column+1] == 0:
                res += 1
            if column-1 < 0 or grid[row][column-1] == 0:
                res += 1
            return res

        ans = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans += get_edges(i, j)
        return ans
