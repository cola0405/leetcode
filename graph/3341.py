# dijastra

import heapq
from typing import List
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n,m = len(moveTime), len(moveTime[0])
        d = [(1,0), (-1,0), (0,1), (0,-1)]
        ans = [[float('inf')]*m for _ in range(n)]
        q = [(0,0,0)]

        while q:
            t,x,y = heapq.heappop(q)
            if x == n-1 and y == m-1: return t
            if t >= ans[x][y]: continue
            ans[x][y] = t
            for k in range(4):
                x1, y1 = x+d[k][0], y+d[k][1]
                if 0 <= x1 < n and 0 <= y1 < m:
                    heapq.heappush(q, (1 + max(t, moveTime[x1][y1]), x1, y1))
        return -1

print(Solution().minTimeToReach([[4,17,0],[63,49,49]]))