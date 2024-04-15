# bfs
from typing import List
from collections import deque, defaultdict
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        RED = 0
        BLUE = 1

        g = defaultdict(list)
        for a,b in redEdges:
            g[a].append((b, RED))
        for a,b in blueEdges:
            g[a].append((b, BLUE))

        q = deque()
        q.append((0,-1))    # -1 will different from RED or BLUE
        already = set()
        ans = [float('inf')]*n
        d = 0
        while q:
            for k in range(len(q)):
                node, color = q.popleft()
                already.add((node, color))
                for nxt, nxt_color in g[node]:
                    if color != nxt_color and (nxt, nxt_color) not in already:
                        q.append((nxt, nxt_color))
                ans[node] = min(ans[node], d)
            d += 1

        for i in range(n):
            if ans[i] == float('inf'):
                ans[i] = -1
        return ans

print(Solution().shortestAlternatingPaths( n = 3, redEdges = [[0,1],[1,2]], blueEdges = []))

