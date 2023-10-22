# 从左往右贪
# 可以有跨度，所以相对比55_1 效率会更高一些

from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums)-1
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(i+nums[i], max_reach)
            if max_reach >= target:
                return True
        return False
print(Solution().canJump([0,2,3]))
