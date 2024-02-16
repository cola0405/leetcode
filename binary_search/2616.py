# binary + greedy

# O(logn * n)
# O(n) if you fit the limit, then cnt += 1
# after the iteration, compare the cnt and the required number

from typing import List
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def fit(gap):
            cnt = 0
            i = 1
            while i < len(nums):
                if (nums[i] - nums[i-1]) <= gap:
                    cnt += 1
                    i += 1
                i += 1
            return cnt >= p

        nums.sort()
        low = 0
        high = int(1e9)
        while low < high:
            mid = (low+high)//2
            if fit(mid):
                high = mid
            else:
                low = mid+1
        return low