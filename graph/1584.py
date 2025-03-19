# kruskal + union-find set （贪心）

from typing import List
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]

        n = len(points)
        edges = []      # (distance, i, j)  i, j are the index of points
        for i in range(n):
            for j in range(i+1, n):
                edges.append((abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1]), i, j))
        edges.sort()
        root = list(range(n))
        ans = 0
        for d, i, j in edges:       # 每次取出最小的边，如果不构成环，则选定
            if find(i) != find(j):
                ans += d
                root[find(i)] = find(j)
        return ans
