# 先种生长时间长的，重叠的时间自然最多
from typing import List
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        flowers = sorted(zip(plantTime, growTime),key=lambda item:item[1], reverse=True)
        day = 0
        extra = 0
        for flower in flowers:
            plant, grow = flower
            cost = plant+grow+1
            day += max(cost - extra, 0)
            if cost <= extra:
                extra -= plant
            else:
                extra = grow+1
        return day-1  # start from day0

print(Solution().earliestFullBloom(plantTime = [27,5,24,17,27,4,23,16,6,26,13,17,21,3,9,10,28,26,4,10,28,2], growTime = [26,9,14,17,6,14,23,24,11,6,27,14,13,1,15,5,12,15,23,27,28,12]))
# print(Solution().earliestFullBloom(plantTime = [1,4,3], growTime = [2,3,1]))