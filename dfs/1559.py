# dfs + avoid previous search
from typing import List
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def dfs(x,y,head,last_x,last_y):
            if x<0 or x>=m or y<0 or y>=n \
                or (x==last_x and y==last_y) or grid[x][y] != head:
                return False
            if (x,y) in cycle:
                return True
            cycle.add((x,y))
            already.add((x,y))
            res = False
            for k in range(4):      # avoid previous search
                nxt_x,nxt_y = x+d[k][0],y+d[k][1]
                if (nxt_x,nxt_y) != (last_x,last_y):
                    res = res or dfs(nxt_x,nxt_y,head,x,y)
            return res

        d = [(0,1),(0,-1),(1,0),(-1,0)]
        m = len(grid)
        n = len(grid[0])
        already = set()
        for i in range(m):
            for j in range(n):
                cycle = set()
                if (i,j) not in already and dfs(i,j,grid[i][j],-1,-1):
                    return True
        return False

print(Solution().containsCycle([["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]))

