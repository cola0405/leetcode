# 仅使用@cache剪枝也可以过
from functools import cache
from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i, total):  # 回溯
            if i == len(nums):
                return 1 if total == target else 0
            return dfs(i+1, total+nums[i]) + dfs(i+1, total-nums[i])
        return dfs(0,0)