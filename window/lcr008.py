# 双指针模拟滑动窗口

from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i,j = 0,0
        total = 0
        ans = float('inf')
        while i < len(nums):
            while j<len(nums) and total < target:
                total += nums[j]
                j += 1
            if total >= target:
                ans = min(ans, j-i)
            total -= nums[i]
            i += 1

        if ans != float('inf'):
            return ans
        return 0

print(Solution().minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))