# heap iteration
# update one by one
from typing import List
from heapq import *
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        pq = [-num for num in nums]
        heapify(pq)
        cur = sum(nums)
        target = cur/2
        ans = 0
        while cur > target:
            top = heappop(pq)
            heappush(pq, top/2)
            cur -= -top/2
            ans += 1
        return ans

print(Solution().halveArray([5,19,8,1]))

