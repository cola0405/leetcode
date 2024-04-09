from typing import List
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        arr = sorted(nums)
        if arr[-1] >= 2*arr[-2]:
            return nums.index(arr[-1])
        return -1
