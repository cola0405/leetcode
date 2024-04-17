# reverse the directed graph + search the parents
from typing import List
from collections import defaultdict
class Solution:
    def checkIfPrerequisite(self, n: int, pre: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def dfs(node):
            if len(t[node]) != 0:
                return t[node]
            res = set()
            for v in g[node]:
                t[v] = dfs(v)
                res |= {v} | t[v]
            return res

        t = defaultdict(set)  # record the recursive pre-course
        g = defaultdict(list)
        for a,b in pre:
            g[b].append(a)
        for i in range(n):
            t[i] = dfs(i)

        ans = []
        for u,v in queries:
            ans.append(True if u in t[v] else False)
        return ans

print(Solution().checkIfPrerequisite(n = 3, pre = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]))
