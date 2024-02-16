# greedy + binary search

from typing import List
class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        def fit(k):
            for i in range(k):
                if nums[i]*2 > nums[-k+i]:
                    return False
            return True

        nums.sort()     # the greedy way is to choose the first k elements
        low = 0
        high = len(nums)//2
        while low < high:       # binary search the first k marked items
            mid = (low+high+1)//2
            if fit(mid):
                low = mid
            else:
                high = mid-1
        return low*2

print(Solution().maxNumOfMarkedIndices([3,5,2,4]))