# 从右往左，只要能够从多边形
# 那就是周长最大的

from typing import List
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        total = sum(nums)

        for i in range(len(nums))[::-1]:
            total -= nums[i]
            if total > nums[i]:
                return total + nums[i]
        return -1