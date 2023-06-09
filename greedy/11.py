# 双指针
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        ans = 0
        while l<r:
            ans = max((r-l)*min(height[l], height[r]), ans)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
