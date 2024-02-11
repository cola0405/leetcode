from typing import List
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [0,0]
        for num in nums1:
            if num in nums2:
                ans[0] += 1
        for num in nums2:
            if num in nums1:
                ans[1] += 1
        return ans