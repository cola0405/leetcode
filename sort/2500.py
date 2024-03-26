from typing import List
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans = 0
        for row in grid:
            row.sort(reverse=True)
        for i in range(len(grid[0])):
            maximum = 0
            for row in grid:
                maximum = max(maximum, row[i])
            ans += maximum
        return ans