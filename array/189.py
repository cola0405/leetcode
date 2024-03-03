from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = nums[:]
        n = len(nums)
        start = k%len(nums)
        for i in range(n):
            nums[(start+i)%n] = tmp[i]

print(Solution().rotate(nums = [1,2,3,4,5,6,7], k = 3))