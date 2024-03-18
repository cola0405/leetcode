# pick up the maximum/miniumum every time
from typing import List
from heapq import *
class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        pq = [(nums[i], i) for i in range(n)]
        heapify(pq)
        abandon = set()
        ans = 0
        while pq:
            score,inx = heappop(pq)
            if inx not in abandon:
                ans += score
                abandon.add(inx)
                abandon.add(inx-1)
                abandon.add(inx+1)
        return ans


print(Solution().findScore([2,1,3,4,5,2]))

