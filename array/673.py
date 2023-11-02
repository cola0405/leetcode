from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        d = [0]*n
        max_len = 1


print(Solution().findNumberOfLIS([1,3,5,4,7]))


