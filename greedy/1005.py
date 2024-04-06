from typing import List
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        for i in range(n):
            if k > 0 and nums[i] < 0:
                nums[i] *= -1
                k -= 1
        nums.sort()
        if k%2 == 0:
            return sum(nums)
        else:
            return sum(nums)-2*nums[0]