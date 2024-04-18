# multi-distance + cycle detection
from typing import List
from collections import deque,defaultdict
class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        def bfs(start):
            # no restriction to the depth of bfs, so don't need nested for-loop
            already = set()
            q = deque([(start, 0)])
            d = [float('inf')]*n
            d[start] = 0
            while q:
                cur, last = q.popleft()
                already.add(cur)
                for nxt in g[cur]:
                    if nxt == last:     # search back detection
                        continue
                    if nxt in already:
                        return d[cur] + d[nxt] + 1
                    # if it can't detect the cycle before it, we can't get shorter cycle
                    if d[cur] >= ans:
                        return float('inf')
                    q.append((nxt, cur))
                    d[nxt] = min(d[nxt], d[cur] + 1)
            return float('inf')

        g = defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        ans = float('inf')
        for node in range(n):
            ans = min(ans, bfs(node))
        return ans if ans != float('inf') else -1

print(Solution().findShortestCycle(n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]))