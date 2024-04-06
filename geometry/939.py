# try left-bottom and right-top
from typing import List
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        n = len(points)
        exist = {(x,y) for x,y in points}
        ans = float('inf')
        for i in range(n):
            for j in range(i+1, n):
                x1,y1 = points[i]
                x2,y2 = points[j]
                if y1 == y2 or x1 == x2:
                    continue
                x3,y3 = x1,y2
                x4,y4 = x2,y1
                if (x3,y3) in exist and (x4,y4) in exist:
                    ans = min(ans, abs(x1-x2)*abs(y1-y2))
        return ans if ans != float('inf') else 0