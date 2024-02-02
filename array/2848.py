from typing import List
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        flags = [0]*101
        for start,end in nums:
            for i in range(start, end+1):
                flags[i] = 1
        return flags.count(1)