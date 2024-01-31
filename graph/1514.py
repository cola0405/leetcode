# Dijkstra + greedy -- choose the highest prob every time
import heapq
from typing import List
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # large amount of nodes -- use hash table
        g = {i: dict() for i in range(n)}
        for i in range(len(edges)):
            a,b = edges[i]
            g[a][b] = succProb[i]
            g[b][a] = succProb[i]

        pq = []  # 10^4 -- we need to use heap to optimize
        heapq.heappush(pq, (-1, start_node))    # default min-heap

        already = set()     # Dijkstra record
        while len(pq) > 0:
            prob,node = heapq.heappop(pq)
            ans = -prob
            if node == end_node:
                return ans
            already.add(node)
            for nxt in g[node]:
                if nxt not in already:
                    heapq.heappush(pq, (ans*-g[node][nxt], nxt))
        return 0

print(Solution().maxProbability(n = 5, edges = [[1,4],[2,4],[0,4],[0,3],[0,2],[2,3]], succProb = [0.37,0.17,0.93,0.23,0.39,0.04], start_node = 3, end_node = 4))