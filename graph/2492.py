# dfs + analyse
# just search the reachable mininal score

from typing import List
from collections import defaultdict
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        def dfs(node):
            nonlocal min_score
            if node in already:
                return
            already.add(node)
            for nxt, s in g[node]:
                min_score = min(min_score, s)
                dfs(nxt)

        already = set()
        g = defaultdict(list)
        for a,b,score in roads:
            g[a].append((b,score))
            g[b].append((a,score))
        min_score = float('inf')
        dfs(1)
        return min_score

print(Solution().minScore(n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]))
