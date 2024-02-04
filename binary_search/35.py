from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)
        while low<high:
            mid = (low+high)//2
            if nums[mid] >= target:
                high = mid
            else:
                low = mid+1
        return low

print(Solution().searchInsert(nums = [1,3,5,6], target = 2))