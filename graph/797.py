from typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        ans = []

        def dfs(cur, path):
            if cur == n-1:
                ans.append(path)
                return
            if len(graph[cur]) == 0:
                return

            for node in graph[cur]:
                dfs(node, path+[node])
        dfs(0, [0])
        return ans

print(Solution().allPathsSourceTarget(graph = [[4,3,1],[3,2,4],[3],[4],[]]))



