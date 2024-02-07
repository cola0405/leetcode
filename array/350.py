from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        ans = []
        for num in cnt1:
            ans += [num] * min(cnt1[num], cnt2[num])
        return ans

