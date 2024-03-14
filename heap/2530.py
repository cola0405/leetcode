from typing import List
from heapq import *
from math import ceil
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        pq = [-num for num in nums]
        heapify(pq)
        ans = 0
        for i in range(k):
            top = heappop(pq)
            ans -= top
            heappush(pq, -ceil(-top/3))
        return ans

print(Solution().maxKelements([1,10,3,3,3], k = 3))
