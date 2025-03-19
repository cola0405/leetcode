'''
dp[i][j] 表示从[0,i]中总和为j的子序列的最大长度
dp[i][j] = -1 表示不存在总和为j的子序列（Ps: 不能设置为0，为了不与初始状态矛盾）

因为这道题nums[i]的范围取得到1000，所以这个dp效率比较低
优化的思路：压缩dp的状态，详见2915_1.py

'''


from typing import List
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[-1]*(target+1) for _ in range(n+1)]
        # 初始状态
        dp[0][0] = 0
        s = 0
        for i in range(1,n+1):
            s = min(s+nums[i-1],target)
            for j in range(s+1):
                if dp[i-1][j] == -1: continue
                dp[i][j] = max(dp[i][j], dp[i-1][j])        # 不选nums[i]
                s = nums[i-1] + j
                if s > target: continue
                dp[i][s] = max(dp[i][s], dp[i-1][j] + 1)   # 选nums[i]
        return dp[n][target]

print(Solution().lengthOfLongestSubsequence(nums = [4,1,3,2,1,5], target = 7))
                