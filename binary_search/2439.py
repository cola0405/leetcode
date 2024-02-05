# binary search + greedy
from typing import List
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def fit(target):
            nums1 = nums[::]
            # from right to left
            for i in range(1, len(nums1))[::-1]:
                if nums1[i] > target:
                    nums1[i-1] += nums1[i] - target
                    nums1[i] = target
            return nums1[0] <= target

        low = min(nums)
        high = max(nums)
        while low < high:
            mid = (low+high)//2
            if fit(mid):
                high = mid
            else:
                low = mid+1
        return low

print(Solution().minimizeArrayValue([3,7,1,6]))