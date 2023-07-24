from typing import List
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1,y1 = rec1[0], rec1[1]
        x2,y2 = rec1[2], rec1[3]
        x3, y3 = rec2[0], rec2[1]
        x4, y4 = rec2[2], rec2[3]

        x_gap = min(x2,x4) - max(x1,x3)
        y_gap = min(y2,y4) - max(y1,y3)

        return x_gap>0 and y_gap>0

print(Solution().isRectangleOverlap([0,0,1,1],
[2,2,3,3]))