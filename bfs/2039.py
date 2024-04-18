# bfs + math
from typing import List
from collections import deque,defaultdict
class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        q = deque([0])
        already = {0}
        g = defaultdict(list)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        d = [-1]*n
        cnt = 0

        # bfs calculate the shortest path
        while q:
            for k in range(len(q)):
                node = q.popleft()
                d[node] = cnt
                for nxt in g[node]:
                    if nxt not in already:
                        already.add(nxt)
                        q.append(nxt)
            cnt += 1

        ans = 0
        for i in range(1, n):
            x = d[i]*2
            ans = max(ans, (x-1)//patience[i]*patience[i]+x)
        return ans+1

print(Solution().networkBecomesIdle( [[0,1],[0,2],[1,2]], patience = [0,10,10]))

