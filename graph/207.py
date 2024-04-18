# topological sorting (queue)
from typing import List
from collections import defaultdict
class Solution:
    def canFinish(self, n: int, pre: List[List[int]]) -> bool:
        after = defaultdict(list)
        in_deg = [0]*n
        for a,b in pre:
            in_deg[a] += 1
            after[b].append(a)
        q = [i for i in range(n) if in_deg[i] == 0]
        remain = n-len(q)
        while q:    # q only contain the available courses
            for k in range(len(q)):
                x = q.pop()
                for v in after[x]:  
                    in_deg[v] -= 1
                    if in_deg[v] == 0:  # update the available courses
                        q.append(v)
                        remain -= 1
        return remain == 0

print(Solution().canFinish(2, [[1,0]]))

