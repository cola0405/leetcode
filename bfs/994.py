# bfs
# bfs -- nodes interaction
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        already = set()
        q1 = []
        fresh = 0
        for i in range(m):
            for j in range(n):
                cur = (i,j)
                if grid[i][j] == 2 and cur not in already:
                    q1.append(cur)
                    already.add(cur)
                if grid[i][j] == 1:     # fresh
                    fresh += 1

        # bfs
        d = [(0,1),(0,-1),(1,0),(-1,0)]
        q2 = []
        ans = 0
        while q1:
            flag = 0
            for inx in range(len(q1)):
                i, j = q1[inx]
                for k in range(4):
                    x, y = i+d[k][0], j+d[k][1]
                    if 0<=x<m and 0<=y<n \
                            and grid[x][y]==1 and (x, y) not in already:
                        q2.append((x, y))
                        already.add((x, y))
                        fresh -= 1
                        flag = 1
            q1 = q2
            q2 = []
            if flag:    # infect or not
                ans += 1
        return ans if fresh == 0 else -1

print(Solution().orangesRotting([[0]]))



