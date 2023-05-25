from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)

        # 忽略第一位
        dp1 = [0] * (n+1)
        for i in range(2, n+1):
            dp1[i] = max(dp1[i-2] + nums[i-1], dp1[i-1])

        # 取第一位
        dp2 = [0] * (n+1)
        dp2[1] = nums[0]
        for i in range(2, n):
            dp2[i] = max(dp2[i-2] + nums[i-1], dp2[i-1])

        return max(dp1[-1], dp2[-2])