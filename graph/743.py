# Dijkstra greedy —— choose the shortest path every time

from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = [[float('inf')]*(n+1) for i in range(n+1)]
        for u,v,time in times:
            g[u][v] = time

        visited = [False] * (n+1)
        t = [float('inf')] * (n+1)
        t[k] = 0
        visited[k] = True

        cur = k
        ans = 0
        remain = n-1
        while remain > 0:
            min_time = float('inf')
            closest_node = -1
            for node in range(1,n+1):
                if not visited[node]:
                    if ans+g[cur][node] < t[node]:      # update the current reachable path
                        t[node] = ans+g[cur][node]
                    if t[node] < min_time:
                        min_time = t[node]
                        closest_node = node

            if min_time == float('inf'):    # no path to go
                return -1

            ans = min_time      # solve the multi-arrived problem
            cur = closest_node      # choose the closest node
            visited[closest_node] = True
            remain -= 1
        return ans

print(Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))




