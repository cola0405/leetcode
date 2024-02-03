from typing import List
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        pre = 0
        ans = 0
        for num in nums:
            pre += num
            if pre > 0:
                ans += 1
        return ans