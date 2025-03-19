# Floyd

# ps: you can't use simple bfs to solve this problem, because the order of visiting the nodes matters
# we need to visit the nodes optimally to get the smallest number of cities under the threshold

# return the smallest number of cities under the threshold
# we can use the Floyd calculate the distance between all cities
# the return the answer


from typing import List
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        g = [[float('inf')]*n for i in range(n)]
        for a,b,w in edges:
            g[a][b] = w
            g[b][a] = w

        dist = [[float('inf')]*n for i in range(n)]
        for a in range(n):
            for b in range(n):
                if a == b:
                    dist[a][b] = 0
                elif g[a][b] != float('inf'):
                    dist[a][b] = g[a][b]

        # Floyd —— use the mid to update the shortest between a and b
        for mid in range(n):
            for a in range(n):
                for b in range(n):
                    dist[a][b] = min(dist[a][b], dist[a][mid] + dist[mid][b])

        # find the node with path <= threshold
        ans = -1
        ans_cnt = float('inf')
        for a in range(n):
            cnt = 0
            for b in range(n):
                if dist[a][b] <= distanceThreshold:
                    cnt += 1
            if cnt <= ans_cnt:
                ans_cnt = cnt
                ans = max(ans, a)
        return ans

print(Solution().findTheCity(n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2))

