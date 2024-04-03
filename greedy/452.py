# must + greedy
# sort the "start"
from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort()
        i = 0
        ans = 0
        while i < n:
            end = points[i][1]
            while i < n and points[i][0] <= end:
                end = min(end, points[i][1])
                i += 1
            ans += 1
        return ans

print(Solution().findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
