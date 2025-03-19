# union-set find + bipartite
from typing import List
from collections import defaultdict
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def find(x):
            if x == group[x]: return x
            group[x] = find(group[x])
            return group[x]

        group = list(range(n+1))
        g = defaultdict(list)
        for a, b in dislikes:
            g[a].append(b)
            g[b].append(a)
        for x in g:
            for nxt in g[x]:
                if find(x) == find(nxt): return False
                group[nxt] = find(g[x][0])
        return True