from typing import List
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        num1 = nums[0]
        for i in range(1, len(nums)):
            for j in range(i+1, len(nums)):
                if num1 < nums[j] < nums[i]:
                    return True
            num1 = min(nums[i], num1)   # 最低点可以定，剩下i、j暴力枚举
        return False