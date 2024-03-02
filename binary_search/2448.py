# U-binary search
from typing import List
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def the_cost(target):
            res = 0
            for num in nums:
                pass
            pass
        low = min(nums)
        high = max(nums)
        while low < high:
            mid = (low+high)//2
            if the_cost(mid) <= the_cost(mid+1):
                high = mid
            else:
                low = mid+1
        return low