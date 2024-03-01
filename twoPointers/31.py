from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            j = i+1
            while j+1 < n and nums[j+1] > nums[i]:
                j += 1
            nums[i], nums[j] = nums[j], nums[i]

        # reverse the right part from decreasing order to ascending order
        i += 1
        for j in range((n-i+1)//2):
            nums[i],nums[n-1-j] = nums[n-1-j], nums[i]
            i += 1
print(Solution().nextPermutation([5,1,1]))



