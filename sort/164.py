# bucket sort
from typing import List
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        maximum = max(nums)
        n = len(str(maximum))
        for k in range(n):
            bucket = [[] for u in range(10)]
            for num in nums:
                digit = num//(10**k) % 10
                bucket[digit].append(num)
            nums = []
            for b in bucket:
                nums += b
        max_gap = 0
        for i in range(len(nums)-1):
            max_gap = max(max_gap, nums[i+1]-nums[i])
        return max_gap