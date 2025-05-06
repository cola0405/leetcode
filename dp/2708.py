from typing import List
class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        mx = mn = nums[0]
        for x in nums[1:]:
            # 这么写是为了让 mx、mn保持上一个状态
            mx, mn = max(mx, x, mx * x, mn * x), min(mn, x, mx * x, mn * x)
        return mx