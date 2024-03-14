# heap-iteration + greedy
# increase the smallest element
# because the contribution is the sum of all other numbers
# [3,7,4,5] -- increase 3 -- profit 7+4+5 is maximum
from typing import List
from heapq import *
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MOD = int(1e9+7)
        pq = nums[:]
        heapify(pq)
        for i in range(k):
            top = heappop(pq)   # increase the smallest element
            heappush(pq, top+1)
        ans = 1
        for num in pq:
            ans = ans*num%MOD
        return ans

print(Solution().maximumProduct(nums = [0,4], k = 5))