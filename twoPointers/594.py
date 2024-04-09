# the condition(limit) may help us sometimes
from typing import List
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        i = 0
        ans = 0
        while i+1 < n:
            while i < n and i-1 >= 0 and nums[i] == nums[i-1]:
                i += 1
            if i >= n:
                break
            j = i+1
            while j < n and nums[j]-nums[i] <= 1:
                j += 1
            if nums[j-1] - nums[i] == 1:
                ans = max(ans, j-i)
            i += 1
        return ans

print(Solution().findLHS([1,1,1,1]))