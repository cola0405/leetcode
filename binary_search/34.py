import bisect
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)-1
        if left == len(nums) or nums[left] != target:
            left = -1
        if 0 <= right < len(nums) and nums[right] != target:
            right = -1
        return [left, right]