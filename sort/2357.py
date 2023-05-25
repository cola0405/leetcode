from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            x = nums[i]
            for j in range(i, len(nums)):
                nums[j] -= x
            count += 1
        return count

print(Solution().minimumOperations(nums = [1,5,0,3,5]))