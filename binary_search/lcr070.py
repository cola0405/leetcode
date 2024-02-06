# special binary search O(logn)
from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        low,high = 0,n-1
        while low < high:   # the unique will change the head's index from even to odd
            mid = (low+high)//2
            head = mid
            if mid-1 >= 0 and nums[mid-1] == nums[mid]:
                head = mid-1
            if head == n-1 or nums[head] != nums[head+1]:
                return nums[head]
            if head%2 != 0:     # if current head's index is not even, it means the unique number must be in left
                high = mid
            else:
                low = mid+1
        return nums[low]

print(Solution().singleNonDuplicate([1,1,2,3,3,4,4,8,8]))