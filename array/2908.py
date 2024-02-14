# prefix + suffix record the minimum elements before and after nums[i]
from typing import List
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0] * n
        left[0] = nums[0]
        for i in range(1, n):
            left[i] = min(left[i-1],nums[i])

        right = [0] * n
        right[-1] = nums[-1]
        for i in range(n-1)[::-1]:
            right[i] = min(right[i+1],nums[i])

        ans = float('inf')
        for i in range(n):
            if nums[i] > left[i] and nums[i] > right[i]:
                ans = min(ans, nums[i]+left[i]+right[i])
        return ans if ans != float('inf') else -1