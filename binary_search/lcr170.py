import heapq
from typing import List
class Solution:
    def reversePairs(self, record: List[int]) -> int:
        pq = record[:]
        heapq.heapify(pq)
        ans = 0
        for num in record:
            s = []
            while heapq.heappop():
                s