# 区间和，前缀和优化
from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        p = [0]
        for num in nums:
            p.append(p[-1]+num)

        n = len(nums)
        for i in range(n):
            if p[i] == p[n]-p[i+1]:
                return i
        return -1

print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))