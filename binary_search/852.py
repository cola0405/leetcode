#  left <- mid -> right  -- to determine is the left part or mid or right part
from typing import List
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        low = 0
        high = n-1
        while low < high:
            mid = (low+high)//2
            if mid+1 < n and arr[mid] < arr[mid+1]:
                low = mid+1
            elif mid-1 >= 0 and arr[mid-1] > arr[mid]:
                high = mid-1
            else:
                return mid
        return low      # the peek count be the endpoint

print(Solution().peakIndexInMountainArray([0,10,5,2]))