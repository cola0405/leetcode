import bisect
from typing import List
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        revered_nums2 = nums2[::-1]
        ans = 0
        for i in range(len(nums1)):
            j = len(nums2)-1-bisect.bisect_left(revered_nums2, nums1[i])
            ans = max(ans, j-i)
        return ans

print(Solution().maxDistance(nums1 = [2,2,2], nums2 = [10,10,1]))