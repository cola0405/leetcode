# prim （dp）

# 维护一个 d 数组，每次选择 d 数组中距离最短的边
# 然后更新加入节点的生成树到其他未达节点的最短距离

from typing import List
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        vis = [0]*n
        d = [float('inf')]*n   # d[i] = 当前生成树到 i 的最短距离
        ans = 0
        node = 0
        d[node] = 0
        for _ in range(n):
            min_cost = float('inf')
            for i in range(n):
                if not vis[i] and d[i] < min_cost:
                    min_cost = d[i]
                    node = i
            vis[node] = 1
            for j in range(n):      # 更新到各个节点的最短距离
                if not vis[j]:
                    d[j] = min(d[j], abs(points[node][0]-points[j][0]) + abs(points[node][1]-points[j][1]))
            ans += min_cost
        return ans

print(Solution().minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
