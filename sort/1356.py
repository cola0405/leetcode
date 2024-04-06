from typing import List
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=lambda item: (bin(item).count('1'), item))
        return arr