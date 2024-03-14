# heap iteration + greedy
from typing import List
from heapq import *
from math import ceil
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        pq = [-p for p in piles]
        heapify(pq)
        for i in range(k):
            top = heappop(pq) * -1
            heappush(pq, -ceil(top/2))
        return -sum(pq)

print(Solution().minStoneSum([5,4,9], k = 2))

