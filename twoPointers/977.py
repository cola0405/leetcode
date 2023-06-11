from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        ans = [0]*len(nums)
        i = len(nums)-1
        while i>=0:
            if nums[left] + nums[right] > 0:
                ans[i] = nums[right]**2
                right -= 1
            else:
                ans[i] = nums[left]**2
                left += 1
            i -= 1
        return ans

print(Solution().sortedSquares(nums = [-4,-1,0,3,10]))