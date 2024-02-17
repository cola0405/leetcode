from typing import List
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def fit(capacity):
            cnt = 0
            i = 0
            while i < len(nums):
                if nums[i] <= capacity:
                    cnt += 1
                    i += 1
                i += 1
            return cnt >= k

        low = 1
        high = int(1e9)
        while low < high:
            mid = (low+high)//2
            if fit(mid):
                high = mid
            else:
                low = mid+1
        return low
