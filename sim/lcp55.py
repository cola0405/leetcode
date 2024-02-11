# easy but good
from typing import List
class Solution:
    def getMinimumTime(self, time: List[int], fruits: List[List[int]], limit: int) -> int:
        from math import ceil
        total_time = 0
        for typ, num in fruits:
            total_time += time[typ]*ceil(num/limit)
        return total_time