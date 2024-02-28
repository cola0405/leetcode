# binary search 2d sorted array
from typing import List
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def count(x):
            n = len(nums)
            cnt = 0
            j = 1
            for i in range(n):
                while j < n and nums[j] - nums[i] <= x:
                    j += 1      # 2d do have the pattern
                cnt += j-i-1
            return cnt

        nums.sort()
        low = 0
        high = max(nums) - min(nums)
        while low < high:
            mid = (low+high)//2
            if count(mid) >= k:
                high = mid
            else:
                low = mid+1
        return low

print(Solution().smallestDistancePair([9,10,7,10,6,1,5,4,9,8],18))