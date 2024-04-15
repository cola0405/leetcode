# dfs O(n^3)
from typing import List
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def dfs(inx):
            already.add(inx)
            detonated.add(inx)
            for i in range(n):
                if (i != inx and i not in detonated
                        and is_detonated(bombs[inx], bombs[i])):
                    dfs(i)

        def is_detonated(a, b):
            return (a[0]-b[0])**2 + (a[1]-b[1])**2 <= a[2]**2

        ans = 1
        n = len(bombs)
        already = set()
        for i in range(n):
            if i in already:
                continue
            detonated = set()
            dfs(i)
            ans = max(ans, len(detonated))
        return ans

print(Solution().maximumDetonation([[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]))