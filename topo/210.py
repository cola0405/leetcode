from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, n: int, pre: List[List[int]]) -> List[int]:
        in_deg = [0]*n
        after = defaultdict(list)
        for a,b in pre:
            in_deg[a] += 1
            after[b].append(a)

        q = [i for i in range(n) if in_deg[i] == 0]
        remain = n-len(q)
        ans = []
        while q:
            x = q.pop()
            ans.append(x)
            for v in after[x]:
                in_deg[v] -= 1
                if in_deg[v] == 0:
                    q.append(v)
                    remain -= 1
        return ans if remain == 0 else []