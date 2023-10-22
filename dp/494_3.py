# 利用set剪枝
from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i, total):  # 回溯
            if i == len(nums):
                return 1 if total == target else 0

            # 剪枝
            pair = (i, total)
            if pair in record:
                return record[pair]
            if total + (prefix[-1] - prefix[i]) < target:
                return 0
            elif total - (prefix[-1] - prefix[i]) > target:
                return 0

            # 记录
            res1 = dfs(i+1, total+nums[i])
            res2 = dfs(i+1, total-nums[i])
            record[(i+1,total+nums[i])] = res1
            record[(i+1,total-nums[i])] = res2

            return res1+res2

        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1]+num)

        record = dict()
        return dfs(0,0)

print(Solution().findTargetSumWays(nums = [9,7,0,3,9,8,6,5,7,6], target = 2))