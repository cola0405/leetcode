# bfs
# dfs also works
from typing import List
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        already = set()     # optimization
        def bfs(x, y):
            q1 = [(x,y)]
            q2 = []
            d = [(-1,1), (0,1), (1,1)]
            move = 0
            while q1:
                flag = 0
                for inx in range(len(q1)):
                    i,j = q1[inx]
                    for k in range(3):
                        x,y = i+d[k][0], j+d[k][1]
                        cur = (x,y)
                        if (0<=x<m and 0<=y<n
                                and grid[x][y] > grid[i][j] and cur not in already):
                            q2.append(cur)
                            already.add(cur)
                            flag = 1
                q1 = q2
                q2 = []
                if flag:
                    move += 1
            return move

        m = len(grid)
        n = len(grid[0])
        ans = 0
        for c in range(m):
            ans = max(ans, bfs(c, 0))
        return ans

print(Solution().maxMoves([[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]))