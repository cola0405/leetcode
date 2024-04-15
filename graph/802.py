# tri-color marking algorithm (cycle detection)
from typing import List
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(node):
            if flags[node] == 2:
                return True

            flags[node] = 1
            for nxt in graph[node]:
                if flags[nxt] == 1:
                    return False
                # only mark the node in dfs, it will not kill the wrong node
                if flags[nxt] == 0 and not dfs(nxt):
                    return False
            flags[node] = 2
            return True

        n = len(graph)
        flags = [0]*n
        for i in range(n):
            if flags[i] == 0:
                dfs(i)
        return [i for i in range(n) if flags[i] == 2]

print(Solution().eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))