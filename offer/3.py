from typing import List
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        already = set()
        for num in nums:
            if num not in already:
                already.add(num)
            else:
                return num
