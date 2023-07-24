# 1/2 * |x1y2 + x2y3 + x3y1 - x2y1 - x3y2 - x1y3|

from typing import List
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        from itertools import combinations
        X = 0
        Y = 1
        ans = 0
        for pair in combinations(points, 3):
            a,b,c = pair
            s = 0.5 * abs(a[X]*b[Y] + b[X]*c[Y] + c[X]*a[Y] - a[X]*c[Y] - b[X]*a[Y] - c[X]*b[Y])
            ans = max(s, ans)
        return ans

print(Solution().largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]))
