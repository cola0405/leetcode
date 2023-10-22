# 转化问题后，题目简化了
# 不再是所有数字都必须选
# 而是选出n个数字来做全减(其余数全加)，如果达到gap，即可完成target
# 此时问题简化某个数字选/不选，进行累加统计 (选+-的话问题会复杂很多，跨度大)
# 而且是gap是单调的计算，不用处理负数的情况

from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        gap = sum(nums) - target  # 把问题转化为:在n个数中减去哪几个数可以得到target
        if gap%2 != 0 or gap<0:  # 如果无法整除，则肯定找不到
            return 0
        gap //= 2       # 问题转换后，gap肯定为正数，省事很多

        # 和为j的方法数
        dp = [[0]*(gap+1) for _ in range(2)]
        dp[0][0] = 1
        last = 0
        cur = 1
        for i in range(n):
            for j in range(gap+1):
                # 当前nums[i]选或不选
                dp[cur][j] = dp[last][j]
                if j-nums[i] >= 0:
                    dp[cur][j] += dp[last][j-nums[i]]
            cur, last = last, cur  # 滚动数组
        return dp[last][gap]

print(Solution().findTargetSumWays(nums = [9,7,0,3,9,8,6,5,7,6], target = 2))