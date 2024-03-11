# sliding window + sorted list
from typing import List
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from sortedcontainers import SortedList
        n = len(nums)
        window = SortedList([nums[0]])
        i = 0
        ans = 1
        for j in range(1,n):
            if abs(nums[j] - window[0]) <= limit and abs(nums[j] - window[-1]) <= limit:
                window.add(nums[j])
                ans = max(ans, len(window))
            else:
                while window and (abs(nums[j] - window[0]) > limit or abs(nums[j] - window[-1]) > limit):
                    window.remove(nums[i])
                    i += 1
                window.add(nums[j])
        return ans

print(Solution().longestSubarray(nums = [1,5,6,7,8,10,6,5,6], limit = 4))
