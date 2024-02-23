from typing import List
class Solution:
    def reversePairs(self, record: List[int]) -> int:
        def merge_sort(l, r):
            if l >= r:
                return 0

            mid = (l+r)//2
            res = merge_sort(l, mid) + merge_sort(mid+1, r)

            nums1 = record[l:mid+1]
            nums2 = record[mid+1:r+1]
            i = j = 0
            inx = 0
            for inx in range(l, r+1):   # count the reversed pair when merge
                if i >= len(nums1) or j >= len(nums2):
                    break
                if nums1[i] > nums2[j]:
                    record[inx] = nums2[j]
                    j += 1
                    res += len(nums1)-i
                else:
                    record[inx] = nums1[i]
                    i += 1
            while i < len(nums1):
                record[inx] = nums1[i]
                inx += 1
                i += 1
            while j < len(nums2):
                record[inx] = nums2[j]
                inx += 1
                j += 1
            return res
        return merge_sort(0, len(record)-1)

print(Solution().reversePairs([9, 7, 5, 4, 6]))

