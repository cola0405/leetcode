# heap -- dealing with the multi-queue problem
from typing import List
class item:
    def __init__(self,i,j,value):
        self.i = i
        self.j = j
        self.value = value
    def __lt__(self, other):
        return self.value < other.value

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        import heapq
        pq = [item(i,0,nums1[i]+nums2[0]) for i in range(len(nums1))]
        heapq.heapify(pq)
        ans = []
        while len(ans) < k:
            top = heapq.heappop(pq)
            i = top.i
            j = top.j
            ans.append([nums1[i], nums2[j]])
            if j+1 < len(nums2):
                heapq.heappush(pq, item(i,j+1,nums1[i]+nums2[j+1]))
        return ans
print(Solution().kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3))