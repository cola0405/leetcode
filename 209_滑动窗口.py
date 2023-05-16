# 求连续区间和与target
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        s = [0]*(n+1)
        for i in range(1,n+1):
            s[i] = s[i-1]+nums[i-1]

        l = 0
        r = 0
        min_len = float('inf')
        while l<=r and r<len(nums):
            if s[r+1]-s[l] < target:
                r += 1
            else:
                min_len = min(r-l+1, min_len)
                l += 1
        if min_len == float('inf'):
            return 0
        return min_len

print(Solution().minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1]))