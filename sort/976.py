from typing import List
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse=True)
        ans = 0
        for i in range(n-2):
            if nums[i+1] + nums[i+2] > nums[i]:
                ans = max(ans, nums[i] + nums[i+1] + nums[i+2])
        return ans
