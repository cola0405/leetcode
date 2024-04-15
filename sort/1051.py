from typing import List
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ans = 0
        excepted = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != excepted[i]:
                ans += 1
        return ans