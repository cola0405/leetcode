from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return target in nums

print(Solution().search([1,0,1,1,1], 0))