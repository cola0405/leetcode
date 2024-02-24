# two pointers of interval to make array sorted
from typing import List
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        right = n-1
        while right-1 >= 0 and arr[right] >= arr[right-1]:
            right -= 1          # right is the head of the longest non-decreasing suffix

        ans = right
        left = 0
        # condition to make sure the left part is sorted
        while left == 0 or (left < n and arr[left-1] <= arr[left]):
            while right < n and arr[left] > arr[right]:     # make sure the arr[right] >= arr[left]
                right += 1
            # remove the elements between (left, right) to make the arr in non-decreasing order
            ans = min(ans, right-left-1)
            left += 1
        return max(0, ans)


print(Solution().findLengthOfShortestSubarray([1,2,3,3,10,1,3,3,5]))