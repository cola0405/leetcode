from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        from collections import defaultdict
        count = defaultdict(int)
        missing, repeat = 0,0
        for num in nums:
            count[num] += 1
            if count[num] == 2:
                repeat = num

        for num in range(1, len(nums)+1):
            if count[num] == 0:
                missing = num
                break
        return [repeat, missing]