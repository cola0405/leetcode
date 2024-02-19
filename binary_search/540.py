# special binary search
from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n-1
        while low < high:       # the unique number will change the parity of index map
            mid = (low+high)//2
            if mid%2 == 0:
                if mid+1 < n and nums[mid] != nums[mid+1]:
                    high = mid
                else:
                    low = mid+1
            else:
                if nums[mid] != nums[mid-1]:
                    high = mid
                else:
                    low = mid+1
        return nums[low]

print(Solution().singleNonDuplicate([1,1,2,3,3]))