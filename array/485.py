from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        i = 0
        while i<len(nums):
            count = 0
            while i<len(nums) and nums[i]:
                count += 1
                i += 1
            ans = max(count, ans)
            i += 1
        return ans

print(Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]))