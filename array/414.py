from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        arr = sorted(list(set(nums)), reverse=True)
        if len(arr) <= 2:
            return arr[0]
        return arr[2]