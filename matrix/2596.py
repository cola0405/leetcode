from typing import List
class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        def check(nxt):
            pair = ((x+1,y+2), (x+2,y+1),
                    (x+1,y-2), (x+2,y-1),
                    (x-1,y+2), (x-2,y+1),
                    (x-1,y-2), (x-2,y-1))

            for dx, dy in pair:
                if ((0 <= dx < n and 0 <= dy < n)
                        and grid[dx][dy] == nxt):
                    return dx, dy
            return x,y

        if grid[0][0] != 0:
            return False

        n = len(grid)
        x = y = 0
        for num in range(1, n*n):
            x1,y1 = check(num)
            if x1 == x and y1 == y:
                return False
            x = x1
            y = y1
        return True

print(Solution().checkValidGrid([[8,3,6],[5,0,1],[2,7,4]]))

