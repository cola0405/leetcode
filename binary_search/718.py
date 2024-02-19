from typing import List
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def fit(n):
            s1 = set()
            for i in range(len(nums1)-n+1):     # O(n^2)
                s1.add(tuple(nums1[i:i+n]))
            s2 = set()
            for i in range(len(nums2)-n+1):
                s2.add(tuple(nums2[i:i+n]))
            return len(s1&s2) > 0

        low = 0
        high = min(len(nums1), len(nums2))
        while low < high:
            mid = (low+high+1)//2
            if fit(mid):
                low = mid
            else:
                high = mid-1
        return low


