# custom heap + multi sorted queue
import heapq
from typing import List
class item:
    def __init__(self, i, j, a, b):
        self.i = i
        self.j = j
        self.a = a
        self.b = b

    def __lt__(self, other):
        return self.a / self.b < other.a / other.b

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        pq = [item(0, i, arr[0], arr[i]) for i in range(1,n)]
        heapq.heapify(pq)
        for u in range(k-1):
            top = heapq.heappop(pq)     # to get the next larger element
            heapq.heappush(pq, item(top.i+1, top.j, arr[top.i+1], arr[top.j]))
        top = heapq.heappop(pq)
        return [top.a, top.b]

print(Solution().kthSmallestPrimeFraction(arr = [1,2,3,5], k = 3))