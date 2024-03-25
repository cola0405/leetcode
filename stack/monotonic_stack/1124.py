# monotonic stack + prefix sum
# turning the problem to -- longest subarray with sum > 0 (T:1,NT:-1)
# we can use monotonic feature to reduce the invalid trials

# select the left endpoints
# the left endpoints will only appear at the prefix decreasing points
# if the pre = [0,-1,-2,-1]
# we prefer the endpoint -1 at left, and we can ignore -1 at right
from typing import List
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        pre = [0]
        ms = [0]    # store the decreasing points (including beginning 0)
        for i in range(n):
            if hours[i] > 8:
                pre.append(pre[-1]+1)
            else:
                pre.append(pre[-1]-1)

            if pre[-1] < pre[ms[-1]]:
                ms.append(i+1)  # prefix offset
        ans = 0
        for i in range(n)[::-1]:
            while ms and pre[i+1] - pre[ms[-1]] > 0:    # determine the index
                ans = max(ans, (i+1)-ms.pop())
        return ans

print(Solution().longestWPI([6,6,9]))