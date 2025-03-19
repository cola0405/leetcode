from typing import List
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        dist = [0] * (n+1)
        dist[start_node] = 1
        for _ in range(n-1):
            for i in range(len(edges)):
                a,b = edges[i]
                if dist[a] * succProb[i] > dist[b]:
                    dist[b] = dist[a] * succProb[i]
                if dist[b] * succProb[i] > dist[a]:
                    dist[a] = dist[b] * succProb[i]
        return dist[end_node]

print(Solution().maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start_node=0, end_node=2))