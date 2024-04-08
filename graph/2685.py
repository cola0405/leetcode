from typing import List
from collections import defaultdict
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            if node in already:
                return
            already.add(node)
            components[tag].append(node)
            for nxt in g[node]:
                dfs(nxt)

        def check_complete(nodes):
            for i in range(len(nodes)):
                for j in range(i+1, len(nodes)):
                    if [nodes[i], nodes[j]] not in edges and [nodes[j],nodes[i]] not in edges:
                        return False
            return True

        already = set()
        g = defaultdict(list)
        components = defaultdict(list)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)

        tag = 0
        for x in range(n):
            dfs(x)
            tag += 1
        ans = 0
        for k in components:
            if check_complete(components[k]):
                ans += 1
        return ans

print(Solution().countCompleteComponents(n = 2, edges = [[1,0]]))
