# prefix + suffix + interval of monotonic stack
from typing import List
class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        if len(maxHeights) == 1:
            return maxHeights[0]    # special

        n = len(maxHeights)
        pre = []
        ms_sum = 0
        ms = [-1]   # co-worker
        for i in range(n):
            while len(ms) > 1 and maxHeights[i] < maxHeights[ms[-1]]:
                j = ms.pop()
                ms_sum -= maxHeights[j] * (j - ms[-1])  # reset the interval
            ms_sum += maxHeights[i] * (i - ms[-1])      # add new lines back
            ms.append(i)
            pre.append(ms_sum)

        suf = []
        ms_sum = 0
        ms = [n]    # co-worker
        for i in range(n)[::-1]:
            while len(ms)>1 and maxHeights[i]<maxHeights[ms[-1]]:
                j = ms.pop()
                ms_sum -= maxHeights[j] * (ms[-1]-j)
            ms_sum += maxHeights[i] * (ms[-1]-i)
            ms.append(i)
            suf.append(ms_sum)
        suf = suf[::-1]

        ans = 0
        for i in range(n-1):
            ans = max(ans, pre[i] + suf[i+1])
        return ans

print(Solution().maximumSumOfHeights([1000000000]))