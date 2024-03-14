from typing import List
from heapq import *

class Ratio:
    def __init__(self,p,t):
        self.p = p
        self.t = t
        self.profit = ((self.p+1)/(self.t+1)) - (self.p/self.t)

    def __lt__(self, other):
        return self.profit > other.profit

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        pq = [Ratio(p, t) for p, t in classes]
        heapify(pq)
        for i in range(extraStudents):
            top = heappop(pq)
            top.p += 1
            top.t += 1
            top.profit = ((top.p+1)/(top.t+1)) - (top.p/top.t)
            heappush(pq, top)

        total = 0
        for item in pq:
            total += item.p / item.t
        return total / len(classes)

print(Solution().maxAverageRatio([[2,4],[3,9],[4,5],[2,10]], extraStudents = 4))