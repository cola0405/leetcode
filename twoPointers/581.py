# adaptive interval
from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i+1 < n and nums[i] <= nums[i+1]:
            i += 1      # longest ascending prefix
        j = n-1
        while j-1 >= 0 and nums[j] >= nums[j-1]:
            j -= 1      # longest ascending suffix

        for u in range(i,j+1):
            while i >= 0 and nums[u] < nums[i]:
                i -= 1
            while j < n and nums[u] > nums[j]:
                j += 1
        return max(j-i-1, 0)


print(Solution().findUnsortedSubarray(nums = [2,1]))