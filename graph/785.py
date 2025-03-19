# union-set find + bipartite
from typing import List
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def find(x):
            if x == color[x]: return x
            color[x] = find(color[x])
            return color[x]

        n = len(graph)
        color = list(range(n))
        for i in range(n):
            for nxt in graph[i]:
                if find(i) == find(nxt): return False   # 如果与 i 相连的节点 nxt 已经在同一集合，说明 i 与 nxt 是同一颜色，故不是二分图
                color[nxt] = find(graph[i][0])      # 将与 i 相连的节点都并入同一集合，表示同一颜色
        return True
