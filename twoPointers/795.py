# valid interval
from typing import List
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ans = 0
        l = r = -1
        for i in range(len(nums)):
            if nums[i] > right:     # l is the invalid endpoint
                l = i
            elif nums[i] >= left:
                r = i               # r is a valid endpoint
            # r-l is the number of the valid interval
            ans += max(0,r-l)   # when nums[i] < left, it can also be included in the valid interval
        return ans

print(Solution().numSubarrayBoundedMax(nums = [2,1,4,3], left = 2, right = 3))