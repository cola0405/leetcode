# 二分+贪心
from typing import List
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def check(available):
            if available < max(nums):
                return False
            the_available = available
            group = 1
            for num in nums:
                if the_available >= num:
                    the_available -= num
                else:
                    group += 1
                    the_available = available-num
            return group<=m

        # 二分找合适的标准，因为标准之左不够，标准之右都可以
        low = 0
        high = sum(nums)
        while low<high:
            mid = (low+high)//2
            if check(mid):
                high = mid
            else:
                low = mid+1
        return low

print(Solution().splitArray([0],
1))