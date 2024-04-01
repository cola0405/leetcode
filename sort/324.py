from typing import List
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        arr = sorted(nums, reverse=True)
        cur = 0
        for i in range(1,n,2):      # greedy
            nums[i] = arr[cur]
            cur += 1
        for i in range(0,n,2):
            nums[i] = arr[cur]
            cur += 1

