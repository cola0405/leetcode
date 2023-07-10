from typing import List
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        for i in range(n-1):
            for j in range(n-1-i):
                if heights[j] < heights[j+1]:
                    heights[j],heights[j+1] = heights[j+1],heights[j]
                    names[j],names[j+1] = names[j+1],names[j]
        return names

print(Solution().sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170]))