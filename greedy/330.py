# 详细解析在 2952.py

from typing import List
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        nums.sort()
        i, s = 0, 0
        ans = 0
        while s < n:
            if i < len(nums) and nums[i] <= s+1:
                s += nums[i]
                i += 1
            else:
                s += s+1
                ans += 1
        return ans

