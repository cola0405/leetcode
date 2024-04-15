from typing import List
from collections import Counter


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        cnt = Counter(map(str, digits))
        ans = []
        for num in range(100, 1000, 2):
            c = Counter(str(num))
            if c <= cnt:
                ans.append(num)
        return ans