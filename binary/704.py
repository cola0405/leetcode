from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low<high:
            mid = (low+high)//2
            if nums[mid] >= target:  # 等号的这个不加1
                high = mid
            else:
                low = mid+1
        if nums[low] == target:
            return low
        return -1

print(Solution().search(nums = [-1,0,3,5,9,12], target = 2))