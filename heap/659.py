# hash table + multi-heap
# heap iteration
from typing import List
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        import heapq
        from collections import defaultdict
        d = defaultdict(list)   # the seq length end with "key"
        for num in nums:
            if len(d[num-1]) > 0:
                prev = heapq.heappop(d[num-1])
                heapq.heappush(d[num], prev+1)
            else:
                heapq.heappush(d[num], 1)
        for k in d:
            if d[k]:
                top = heapq.heappop(d[k])
                if top < 3:
                    return False
        return True

print(Solution().isPossible([5,6,7,7,8,8,9,10,11,12]))