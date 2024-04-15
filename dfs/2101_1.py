# optimization -- build the table first
from typing import List
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def dfs(inx):
            already.add(inx)
            detonated.add(inx)
            for nxt in d[inx]:
                if nxt not in detonated:
                    dfs(nxt)

        def is_detonated(a, b):
            return (a[0]-b[0])**2 + (a[1]-b[1])**2 <= a[2]**2

        def detonated_detect():
            res = [[] for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if i != j and is_detonated(bombs[i], bombs[j]):
                        res[i].append(j)
            return res

        n = len(bombs)
        d = detonated_detect()
        ans = 1
        already = set()
        for i in range(n):
            if i in already: continue
            detonated = set()
            dfs(i)
            ans = max(ans, len(detonated))
        return ans

print(Solution().maximumDetonation([[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]))