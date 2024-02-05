from typing import List
class Solution:
    def twoSum(self, price: List[int], target: int) -> List[int]:
        s = set()
        for a in price:
            b = target-a
            if b in s:
                return [a,b]
            s.add(a)

