# topological sort (bfs from outside to inside)
# delete the leaf nodes layer by layer, until only 1 or 2 nodes left
# they are the possible root for Minimum Height Trees

# len(ans) <= 2  -- if len(ans) >= 3, which means there still exist a tree

from typing import List
from collections import defaultdict, deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))

        remain = n
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        degree = [len(g[i]) for i in range(n)]
        q = deque([i for i in range(n) if degree[i] == 1])
        while q:    # store leaf nodes
            remain -= len(q)
            for k in range(len(q)):
                x = q.popleft()
                degree[x] = -1  # -1 means this node has been deleted
                for y in g[x]:
                    degree[y] -= 1
                    if degree[y] == 1 and remain > 2:
                        q.append(y)
            # special case: when only two nodes left, these two nodes both can become the root
            if remain == 2:
                return [x for x in range(n) if degree[x] == 1]
        return [node for node in range(n) if degree[node] == 0]

print(Solution().findMinHeightTrees(n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]))