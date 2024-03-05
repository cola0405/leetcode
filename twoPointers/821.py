# mid diffusion
from typing import List
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [float('inf')]*n
        for i in range(n):
            if s[i] == c:
                ans[i] = 0
                l = i-1
                d = 1
                while l >= 0 and s[l] != c:
                    ans[l] = min(ans[l],d)
                    d += 1
                    l -= 1
                r = i+1
                d = 1
                while r < n and s[r] != c:
                    ans[r] = d
                    d += 1
                    r += 1
        return ans

print(Solution().shortestToChar(s = "loveleetcode", c = "e"))