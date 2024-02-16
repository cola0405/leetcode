# binary search + sliding window

# contiguous subarray, and the final window must be made of (equal numbers + deleted elements)
# longest -- upper bound -- so we can binary search the maximum number of equal numbers
# the window size could be (mid+k)

from typing import List
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        def fit(target):
            window_size = target + k
            cnt = defaultdict(int)
            for i in range(min(window_size, len(nums))):
                cnt[nums[i]] += 1
                if cnt[nums[i]] >= target:
                    return True
            i = 0
            for j in range(window_size, len(nums)):
                cnt[nums[i]] -= 1
                cnt[nums[j]] += 1
                if cnt[nums[j]] >= target:
                    return True
                i += 1
            return False

        low = 1
        high = len(nums)
        while low < high:
            mid = (low+high+1)//2
            if fit(mid):
                low = mid
            else:
                high = mid-1
        return low

print(Solution().longestEqualSubarray(nums = [1,3,2,3,1,3], k = 3))