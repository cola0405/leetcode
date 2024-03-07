# monotonic stack -- (no pop, only push the valid elements)
# O(n) -- the maximum size of the stack is N so it's not O(n^2)
from typing import List
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        s = [0]
        for i in range(n):
            if nums[i] < nums[s[-1]]:
                s.append(i)     # only the smaller num after nums[0] has opportunity
        ans = 0
        for i in range(n)[::-1]:
            while s and nums[i] >= nums[s[-1]]:
                ans = max(ans, i-s[-1])
                s.pop()
        return ans

print(Solution().maxWidthRamp([6,0,8,2,1,5]))