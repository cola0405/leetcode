from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_height = 0
        s = 0
        for h in gain:
            s += h
            max_height = max(s, max_height)
        return max_height
