# sort + sliding window

# the subarray here no need to be contiguous, and the equal elements is discrete(离散的)
# so we do can sort the nums, and the equal elements must be contiguous and could be in a window
# the window's size is the answer
# the way to control the window is -- make sure (maximum - minimum) <= 2*k

from typing import List
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = j = 0
        ans = 0
        while i < len(nums):
            while j < len(nums) and (nums[j] - nums[i]) <= 2*k:
                ans = max(ans, j-i+1)
                j += 1
            i += 1
        return ans

print(Solution().maximumBeauty(nums = [13,46,71], k = 29))