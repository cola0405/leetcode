from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        for item in s:
            if i<len(g) and item >= g[i]:
                i += 1
        return i

print(Solution().findContentChildren(g = [1,2,3], s = [1,1]))
