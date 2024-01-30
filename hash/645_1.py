from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        from collections import Counter
        count = Counter(nums)
        missing, repeat = 0,0

        for num in range(1, len(nums)+1):
            if count[num] == 0:
                missing = num
            elif count[num] == 2:
                repeat = num
        return [repeat, missing]