# 真二分。。。
# 大于0的小于0的，以logN的效率割开

# 这题数据规模小，用不着二分
from typing import List
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        while low<high and nums[high]>0:
            mid = (low+high) // 2
            if nums[mid] > 0:
                high = mid
            else:
                low = mid+1
        # make sure pos is the left end of positive number
        if nums[high] > 0:
            pos = len(nums)-high
        else:
            pos = 0
        while high >= 0 and nums[high] >= 0:
            high -= 1
        if nums[high]<0:
            neg = high+1
        else:
            neg = 0
        return max(neg, pos)

print(Solution().maximumCount([0]))
