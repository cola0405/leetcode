from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        for _ in range(len(nums)):
            if nums[i] == 0:
                nums.append(nums.pop(i))
            else:
                i += 1
        print(nums)

Solution().moveZeroes(nums = [0,1,0,3,12])