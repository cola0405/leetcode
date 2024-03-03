# greedy
from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        tmp = sorted(nums)
        n = len(nums)
        i = 0
        while i < n and nums[i] == tmp[i]:
            i += 1
        j = n-1
        while j >= 0 and nums[j] == tmp[j]:
            j -= 1
        return max(j-i+1, 0)

print(Solution().findUnsortedSubarray(nums = [2,6,4,8,10,9,15]))