from heapq import *
from collections import deque
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        pq = [-ord(ch) for ch in s]
        heapify(pq)
        ans = []
        wait = []
        while pq or wait:
            while len(wait) > 0 and len(pq) > 0:
                ans += chr(-heappop(pq))
                for k in range(repeatLimit):
                    if len(wait) == 0:
                        break
                    ans.append(chr(-wait.pop()))
            if len(pq) == 0:
                break
            cur = chr(-pq[0])
            cnt = 0
            while pq and chr(-pq[0]) == cur and cnt < repeatLimit:
                top = chr(-heappop(pq))
                ans.append(top)
                cnt += 1
            while pq and cnt == repeatLimit and chr(-pq[0]) == ans[-1]:
                wait.append(heappop(pq))
        return ''.join(ans)



print(Solution().repeatLimitedString(s = "aababab", repeatLimit = 2))
