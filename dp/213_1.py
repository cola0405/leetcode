from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(vals):
            pre, cur = 0, 0
            for val in vals:  # 当gap固定时，不需要dp数组，变量足矣
                cur, pre = max(pre + val, cur), cur
            return cur

        if len(nums) == 1:
            return nums[0]
        return max(dp(nums[:-1]), dp(nums[1:]))

print(Solution().rob([2,3]))