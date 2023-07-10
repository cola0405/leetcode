from typing import List
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        idx = list(range(len(heights)))
        idx.sort(key=lambda i: heights[i], reverse=True)
        return [names[i] for i in idx]

print(Solution().sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170]))