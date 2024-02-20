# crazy binary search

from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        while low < high:
            mid = (low+high)//2
            if nums[mid] > nums[high]:
                low = mid+1
            elif nums[mid] < nums[high]:
                high = mid
            else:
                high -= 1
        return nums[low]

print(Solution().findMin([1,3,5]))