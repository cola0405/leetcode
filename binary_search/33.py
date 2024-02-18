from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n-1
        while low < high:
            mid = (low+high)//2
            if nums[mid] > nums[0]:
                low = mid
            else:
                high = mid-1

        # find the upper bound of the number that greater than nums[0]
        if low == n-1:

        high = low
        low = 0
        if target < nums[0]:
            low = high+1
            high = n-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid+1
        return -1

print(Solution().search(nums = [1,3], target = 3))