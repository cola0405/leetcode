# dijastra
# 可以帮我们解决节点访问顺序的问题 -- 按最优顺序访问节点

import heapq
from typing import List
from collections import defaultdict
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        def bfs(node):
            q = [(-distanceThreshold, node)]    # 按照从大到小排序，优先选择剩余"能量"最大的节点
            vis = [0]*n
            while q:
                d, x = heapq.heappop(q)
                d *= -1
                vis[x] = 1
                for nxt in g[x]:
                    if g[x][nxt] <= d and not vis[nxt]:
                        heapq.heappush(q, (-(d-g[x][nxt]), nxt))
            return sum(vis)-1

        g = defaultdict(dict)
        for a,b,w in edges:
            g[a][b] = w
            g[b][a] = w
        ans = (0,float('inf'))
        for city in range(n):
            res = bfs(city)
            if res <= ans[1]: ans = (city, res)
        return ans[0]

print(Solution().findTheCity(n = 6, edges = [[0,1,10],[0,2,1],[2,3,1],[1,3,1],[1,4,1],[4,5,10]], distanceThreshold = 20))

