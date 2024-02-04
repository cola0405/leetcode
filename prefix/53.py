from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = nums[0]
        max_sum = nums[0]
        n = len(nums)
        for i in range(1,n):
            if s < 0:
                s = 0
            s += nums[i]
            max_sum = max(s, max_sum)

        return max_sum

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))