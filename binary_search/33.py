# sorted segments + binary search
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n-1
        if nums[-1] < nums[0]:      # which means nums is rotated
            if target == nums[0]:
                return 0
            while low < high:
                mid = (low+high+1) // 2     # upper bound
                if nums[mid] >= nums[0]:
                    low = mid
                else:
                    high = mid-1
            if target > nums[0]:       # determine the target in which segment
                high = low
                low = 0
            else:
                low = high+1
                high = n-1

        while low <= high:      # binary search the target
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid+1
        return -1

print(Solution().search(nums = [3,1], target = 1))