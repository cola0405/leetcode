from typing import List
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = [0]*len(queries)
        for point in points:
            x,y = point
            for i in range(len(queries)):
                px,py,r = queries[i]
                if (x-px)**2 + (y-py)**2 <= r**2:
                    ans[i] += 1
        return ans

print(Solution().countPoints(points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]))


