# radix sort
from typing import List
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        maximum = max(nums)
        n = len(str(maximum))   # the number of digits
        for k in range(n):
            radix = [[] for u in range(10)]     # [[], [], [],...,[]] len=10
            for num in nums:
                digit = num//(10**k) % 10       # get the kth digit
                radix[digit].append(num)        # put the num into the correct array
            nums = []
            for b in radix:
                nums += b                       # connect those 10 array
        max_gap = 0
        for i in range(len(nums)-1):
            max_gap = max(max_gap, nums[i+1]-nums[i])
        return max_gap
