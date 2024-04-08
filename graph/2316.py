from typing import List
from collections import defaultdict
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def dfs(x):
            if x in already:
                return
            already.add(x)
            block[tag] += 1
            for nxt in g[x]:
                dfs(nxt)

        already = set()
        g = defaultdict(list)
        block = defaultdict(int)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        tag = 0
        for node in g:
            if node not in already:
                dfs(node)
                tag += 1

        # single node
        for node in range(n):
            if node not in already:
                block[tag] += 1
                tag += 1

        # prefix sum calculate the combination
        block = list(block.values())
        pre = [0]
        for num in block:
            pre.append(num+pre[-1])
        ans = 0
        for i in range(len(block))[::-1]:
            ans += block[i] * pre[i]
        return ans

print(Solution().countPairs(n = 12, edges = [[2,6],[11,3],[5,4],[9,6]]))