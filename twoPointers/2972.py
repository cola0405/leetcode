from typing import List
class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i+1 < n and nums[i] < nums[i+1]:
            i += 1      # tail of the longest strictly increasing prefix
        if i == n-1:
            return n*(n+1)//2

        j = n-1
        ans = i+2      # remove the interval (i,j) not including the endpoints
        while j == n-1 or (j >= 0 and nums[j] < nums[j+1]):
            while i >= 0 and nums[i] >= nums[j]:        # strictly increasing order
                i -= 1
            ans += i+2
            j -= 1      # try every j
        return ans

print(Solution().incremovableSubarrayCount( [1,2,3,4]))

