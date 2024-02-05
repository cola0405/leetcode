from typing import List
class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        diff = sum(array1) - sum(array2)
        if diff % 2 != 0:
            return []

        diff //= 2  # for swap
        s = set(array2)
        for num in array1:
            if num - diff in s:     # equation num1-num2=diff
                return [num, num-diff]
        return []