from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        inx = dict()
        for i in range(len(numbers)):
            a = numbers[i]
            b = target - a
            if b in inx:
                return [inx[b],i]
            inx[a] = i