from typing import List
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        pre = nums[0]
        for i in range(1,len(nums)):
            if nums[i-1] + 1 != nums[i]:
                break
            pre += nums[i]
        while True:
            if pre not in nums:
                return pre
            pre += 1