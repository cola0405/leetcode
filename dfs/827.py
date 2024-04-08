# dfs mark
from typing import List
from collections import defaultdict
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def dfs(x,y,t):
            if (x<0 or x>=m or y<0 or y>=n
                    or (x,y) in already or grid[x][y] == 0):
                return
            grid[x][y] = t
            area[t] += 1
            already.add((x,y))
            dfs(x+1,y,t)
            dfs(x-1,y,t)
            dfs(x,y+1,t)
            dfs(x,y-1,t)

        area = defaultdict(int)
        m = len(grid)
        n = len(grid[0])
        already = set()
        tag = -1
        # mark the islands and calculate the area of each island
        for i in range(m):
            for j in range(n):
                if (i,j) not in already:
                    dfs(i,j,tag)
                    tag -= 1

        # merge
        d = [(0,1),(0,-1),(1,0),(-1,0)]
        ans = max(area.values()) if len(area)>0 else 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    s = set()
                    for k in range(4):
                        x,y = i+d[k][0],j+d[k][1]
                        if 0<=x<m and 0<=y<n:
                            s.add(grid[x][y])
                    a = 1
                    for t in s:
                        a += area[t]
                    ans = max(ans, a)
        return ans

print(Solution().largestIsland([[1,0],[0,1]]))