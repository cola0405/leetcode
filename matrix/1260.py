from typing import List
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        res = [[0]*len(grid[0]) for _ in range(len(grid))]
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                res[(i+(j+k)//m)%n][(j+k)%m] = grid[i][j]
        return res

print(Solution().shiftGrid([[1],[2],[3],[4],[7],[6],[5]], k = 23))


