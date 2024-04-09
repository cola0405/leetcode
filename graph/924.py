# dfs
from typing import List
class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        def dfs(node):
            if node in infected:
                return
            infected.add(node)
            for inx in range(n):
                if graph[node][inx] == 1:
                    dfs(inx)

        n = len(graph)
        k = len(initial)
        initial.sort()  # make sure return the smallest node
        cnt = float('inf')
        ans = n
        for i in range(k):      # brute force
            infected = set()
            for j in range(k):  # even though it's dfs in a loop, but still O(n) -- only search the graph
                if i != j:
                    dfs(initial[j])
            if len(infected) < cnt:
                ans = initial[i]
                cnt = len(infected)
        return ans      # return the minimal nodes

print(Solution().minMalwareSpread([[1,1,0],[1,1,0],[0,0,1]],[0,1,2]))
