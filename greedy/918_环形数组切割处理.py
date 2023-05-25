# 先后顺序影响结果，不可贪心
# 最值问题，考虑dp
# dp[i]
# 贪心不够，一维dp解决不了问题
# dp[i][k] 以i结尾长度为k的值有点奇怪
# dp[i] 以i结尾的最大和,len(dp) = 2n
# 但是这样在过环边界的时候会出问题。。没办法把长度圈定。。。直接dp一样没办法解题

# 开始抽象问题
# 最值情况分两种情况：
# ①：max_sub不跨交界 -- 这个容易求
# ②：max_sub跨交界 -- 此时，max_sub = sum - min_sub(必定是不跨界的)

# 上面两者取最大值就是答案
from typing import List
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sub = -float('inf')
        max_cur = -float('inf')
        min_sub = float('inf')
        min_cur = float('inf')

        for num in nums:
            max_cur = max(max_cur+num, num)
            max_sub = max(max_cur, max_sub)

            min_cur = min(min_cur+num, num)
            min_sub = min(min_cur, min_sub)

        ans1 = max_sub
        ans2 = sum(nums)-min_sub
        if ans2 == 0:
            return ans1
        return max(ans1, ans2)

print(Solution().maxSubarraySumCircular(nums = [-3,-2,-3]))