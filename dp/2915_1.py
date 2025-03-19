from typing import List
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        dp = [0] + [-inf] * target      # dp[i] 表示和为i的最长子序列的长度
        s = 0
        for x in nums:                      # 枚举新数字
            s = min(s+x, target)            # dp 刚进入这里的状态是上一轮的状态，所以这里要从右往左dp
            for i in range(x, s+1)[::-1]:   # 从右往左dp
                if dp[i] < dp[i-x] + 1:
                    dp[i] = dp[i-x] + 1
        return dp[-1] if dp[-1] > 0 else -1

print(Solution().lengthOfLongestSubsequence(nums = [4,1,3,2,1,5], target = 7))
                