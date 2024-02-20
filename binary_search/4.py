from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 == 0:
            if n2%2 != 0:
                return nums2[n2//2]
            else:
                return (nums2[(n2-1)//2] + nums2[(n2-1)//2+1]) / 2

        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)

        k = (n1+n2)//2
        low = 0
        high = n1-1
        while low < high:
            m1 = (low+high)//2
            m2 = k-m1-1
            if nums1[m1] < nums2[m2]:
                low = m1+1
            elif nums1[m1] >= nums2[m2]:
                high = m1
        m1 = low
        m2 = k-m1-1
        if (n1+n2)%2 != 0:
            if nums1[m1] < nums2[m2]:
                return nums2[m2]
            else:
                if m2+1 < n2 and nums1[m1] > nums2[m2+1]:
                    return nums2[m2+1]
                return nums1[m1]
        else:
            if nums1[m1] < nums2[m2] and m2-1 >= 0 and nums2[m2-1] > nums1[m1]:
                return (nums2[m2] + nums2[m2-1]) / 2
            if m2+1 < n2 and nums1[m1] > nums2[m2+1]:
                return (nums2[m2] + nums2[m2+1]) / 2

            if m1-1 >= 0 and nums1[m1-1] > nums2[m2]:
                return (nums1[m1]+nums1[m1-1])/2
            else:
                return (nums1[m1] + nums2[m2]) / 2

print(Solution().findMedianSortedArrays(nums1 = [2,4], nums2 = [1,3]))
# nums1 = [1], nums2 = [2,3]
#