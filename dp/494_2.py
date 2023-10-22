# 借助@cache + 前缀和剪枝

from functools import cache
from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i, total):  # 回溯
            if i == len(nums):
                return 1 if total == target else 0
            # 后面的数字全加上都救不了，那就没必要搜下去了
            if total + (prefix[-1] - prefix[i]) < target:
                return 0
            elif total - (prefix[-1] - prefix[i]) > target:
                return 0
            return dfs(i+1, total+nums[i]) + dfs(i+1, total-nums[i])

        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1]+num)

        return dfs(0,0)


print(Solution().findTargetSumWays(nums = [9,7,0,3,9,8,6,5,7,6], target = 2))