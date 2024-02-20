# two pointers
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        same = 1
        for j in range(1,len(nums)):    # nums[i] is ready to be filled
            if nums[j] == nums[i-1] and same == 2:
                continue
            if nums[i-1] == nums[j]:
                same += 1
            nums[i] = nums[j]
            if nums[i] != nums[i-1]:
                same = 1
            i += 1
        return i

print(Solution().removeDuplicates([0,0,1,1,1,1,2,2,2,4]))