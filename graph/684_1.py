from typing import List
from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        g = defaultdict(list)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)

        def count(node):  # count the neighbor nodes
            stack = [node]
            visit = [0]*(n+1)
            while len(stack)>0:
                top = stack.pop()
                visit[top] = 1
                stack += [node for node in g[top] if visit[node]==0]
            return visit.count(1)

        for i in range(n)[::-1]:
            a,b = edges[i]
            g[a].remove(b)
            g[b].remove(a)
            if count(a) == n or count(b) == n:
                return edges[i]
            g[a].append(b)
            g[b].append(a)

print(Solution().findRedundantConnection(edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]))

