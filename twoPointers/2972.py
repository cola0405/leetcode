from typing import List
class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        right = n-1
        while right-1 >= 0 and nums[right] > nums[right-1]:
            right -= 1
        ans = 0
        left = 0
