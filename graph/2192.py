from typing import List
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # build graph
        from collections import defaultdict
        g = defaultdict(list)
        for a,b in edges:
            g[a].append(b)

        ans = [[] for _ in range(n)]
        visit = set()
        for node in range(n):
            visit.add(node)
            stack = g[node][:]
            while len(stack)>0:
                top = stack.pop()
                if top in visit:
                    continue
                visit.add(top)
                ans[top].append(node)
                stack += [p for p in g[top] if p not in visit]
        return ans

print(Solution().getAncestors(n = 8, edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]))