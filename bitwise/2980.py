# just check the last bit
from typing import List
class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                num = nums[i] | nums[j]
                if num&1 == 0:
                    return True
        return False

print(Solution().hasTrailingZeros([1,3,5,7,9]))