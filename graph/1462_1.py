# topology sort
from typing import List
from collections import defaultdict, deque
class Solution:
    def checkIfPrerequisite(self, n: int, pre: List[List[int]], queries: List[List[int]]) -> List[bool]:
        t = defaultdict(set)  # record the recursive pre-course
        after = defaultdict(list)
        in_deg = [0]*n
        for a,b in pre:
            after[a].append(b)
            in_deg[b] += 1
        q = deque([i for i in range(n) if in_deg[i] == 0])
        while q:    # only store the available courses
            x = q.pop()
            for v in after[x]:  # merge the t[x] to after nodes
                t[v] |= {x} | t[x]
                in_deg[v] -= 1
                if in_deg[v] == 0:
                    q.append(v)

        ans = []
        for u,v in queries:
            ans.append(True if u in t[v] else False)
        return ans

print(Solution().checkIfPrerequisite(n = 3, pre = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]))
