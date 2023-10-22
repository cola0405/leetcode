# 因为状态只与左边的状态有关
# 所以可以从右往左优化到一维dp

from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        gap = sum(nums) - target  # 把问题转化为:在n个数中减去哪几个数可以得到target
        if gap%2 != 0 or gap<0:  # 如果无法整除，则肯定找不到
            return 0
        gap //= 2       # 问题转换后，gap肯定为正数，省事很多

        # 和为j的方法数
        dp = [0] * (gap+1)
        dp[0] = 1
        for i in range(n):
            for j in range(gap+1)[::-1]:
                if j >= nums[i]:
                    dp[j] += dp[j-nums[i]]
        return dp[gap]

print(Solution().findTargetSumWays(nums = [9,7,0,3,9,8,6,5,7,6], target = 2))