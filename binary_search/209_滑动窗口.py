# 求连续区间和与target
from typing import List
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')
        s = l = r = 0  # s为滑动窗口各数之和
        while r<n or s>=target:  # or 的这个条件是为了最后压缩滑动窗口
            if s < target and r<n:
                s +=nums[r]
                r += 1
            else:
                ans = min(r-l, ans)
                s -= nums[l]
                l += 1
        return ans if ans!=float('inf') else 0

print(Solution().minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1]))