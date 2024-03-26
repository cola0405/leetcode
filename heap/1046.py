from typing import List
from heapq import *
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-s for s in stones]
        heapify(pq)
        while len(pq) > 1:
            a = -heappop(pq)
            b = -heappop(pq)
            if a != b:
                heappush(pq, -abs(a-b))
        return -pq[0] if pq else 0