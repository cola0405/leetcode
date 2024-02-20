# extreme inplace space + two pointers
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m)[::-1]:    # use the space
            nums1[i-m] = nums1[i]
        i = len(nums1)-m
        j = 0
        cur = 0
        for cur in range(n+m):
            if i >= len(nums1) or j >= len(nums2) or m == 0:
                break
            if nums1[i] < nums2[j]:
                nums1[cur] = nums1[i]
                i += 1
            else:
                nums1[cur] = nums2[j]
                j += 1
        while cur < len(nums1) and j < len(nums2):
            nums1[cur] = nums2[j]
            cur += 1
            j += 1

print(Solution().merge(nums1 = [4,0,0,0,0,0], m = 1, nums2 = [1,2,3,5,6], n = 5))