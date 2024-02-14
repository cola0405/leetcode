# enumerate mid + prefix + suffix

from typing import List
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0]*n
        left[0] = nums[0]
        for i in range(1,n):
            left[i] = max(left[i-1], nums[i])

        right = [0]*n
        right[-1] = nums[-1]
        for i in range(n-1)[::-1]:
            right[i] = max(right[i+1], nums[i])

        ans = 0
        for j in range(1,n-1):
            ans = max(ans, (left[j-1]-nums[j])*right[j+1])
        return ans

print(Solution().maximumTripletValue([12,6,1,2,7]))
