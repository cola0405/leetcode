# sort确认点的排列，然后通过斜率关系判断是否为矩形
# 误差问题的解决：允许一定的误差范围
# abs(k1*k2 - -1) < 1e-6
from typing import List
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        from decimal import Decimal
        def k(a,b):
            if a[0] == b[0]:
                return Decimal('inf')
            return Decimal((a[1]-b[1]) / (a[0]-b[0]))

        points = [p1, p2, p3, p4]
        points.sort()
        p1, p2, p3, p4 = points
        k1 = k(p1,p2)
        k2 = k(p1,p3)
        k3 = k(p4,p2)
        k4 = k(p4,p3)

        s1 = (p2[1]-p1[1])**2 + (p2[0]-p1[0])**2
        s2 = (p3[1]-p1[1])**2 + (p3[0]-p1[0])**2
        s3 = (p4[1]-p2[1])**2 + (p4[0]-p2[0])**2
        s4 = (p4[1]-p3[1])**2 + (p4[0]-p3[0])**2
        if ((k1==Decimal('inf') and k2 == Decimal(0)) or (abs(k1*k2 - -1) < 1e-6))\
            and ((k3==Decimal(0) and k4 == Decimal('inf')) or (abs(k3*k4 - -1) < 1e-6))\
                and (s1 == s2 == s3 == s4):
            return True
        return False



print(Solution().validSquare([1,1],
[5,3],
[3,5],
[7,7]))