# binary search can not only search the answer, but also the target item
import bisect
from typing import List
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            # find the lower bound and upper bound of possible interval
            left = max(i+1, bisect.bisect_left(nums, lower-nums[i]))
            right = max(i+1, bisect.bisect_right(nums, upper-nums[i]))
            ans += right - left
        return ans

print(Solution().countFairPairs(nums = [0,1,7,4,4,5], lower = 3, upper = 6))