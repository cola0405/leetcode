# 二分+贪心
from typing import List
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def limit_available(limit):
            if limit < max(nums):
                return False
            interval_sum = 0
            count = 0
            for i in range(len(nums)):
                if interval_sum+nums[i]<=limit:
                    interval_sum += nums[i]
                else:
                    interval_sum = nums[i]
                    count += 1

            if interval_sum > 0:  # deal with the end
                count += 1

            return count <= k

        low = 0
        high = sum(nums)
        while low<high:
            mid = (low+high)//2  # lower bound 取low
            if limit_available(mid):
                high = mid
            else:
                low = mid+1
        return low

print(Solution().splitArray([0],
1))