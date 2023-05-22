from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(range(1,len(nums)+1))
        nums = set(nums)
        return list(s-nums)

print(Solution().findDisappearedNumbers(nums = [4,3,2,7,8,2,3,1]))




