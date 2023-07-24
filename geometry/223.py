class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        x_gap = min(ax2, bx2) - max(ax1, bx1)
        y_gap = min(ay2, by2) - max(ay1, by1)

        overlap = 0
        if x_gap>0 and y_gap>0:
            overlap = x_gap*y_gap

        s1 = (ax2-ax1) * (ay2-ay1)
        s2 = (bx2-bx1) * (by2-by1)

        return s1+s2-overlap

print(Solution().computeArea(ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2))