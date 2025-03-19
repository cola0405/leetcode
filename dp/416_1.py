# dp 大体思路与dfs一致，只不过dfs是从后往前搜，dp是从前往后搜
# 主要是因为 nums[i] 的取值范围不大，故可以暴力dp
from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        s = sum(nums)
        if s%2 == 1: return False
        target = s//2
        dp = [[0]*(target+1) for _ in range(len(nums)+1)]   # dp[i][j]表示从[0,i]是否存在和为j的子序列
        dp[0][0] = 1    
        for i in range(1,n+1):
            for j in range(target+1):       # 0 到 target 都dp搜一遍
                if dp[i-1][j] == 0: continue
                dp[i][j] = dp[i-1][j]     # 不选nums[i]
                s1 = nums[i-1] + j        # 选nums[i]
                if s1 == target: return True
                if s1 > target: continue     # 不能直接break 可能会使得部分dp[i]没更新到
                dp[i][s1] = 1
        return False

print(Solution().canPartition([18,17,18,11,15,4,13,11,9]))
                