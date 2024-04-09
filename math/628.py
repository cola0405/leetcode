# analyse
# only three situation for nums:
# 1.all negative -- p2*nums[-3]
# 2.one positive -- p1*nums[-1]
# 3.two positive -- p2*nums[-3]
from typing import List
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        p1 = nums[0]*nums[1]
        p2 = nums[-1]*nums[-2]
        return max(p1*nums[-1], p2*nums[-3])

