from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        dist = [(points[i][0]**2+points[i][1]**2, i) for i in range(n)]
        dist.sort()
        ans = []
        for d,inx in dist[:k]:
            ans.append(points[inx])
        return ans

print(Solution().kClosest(points = [[1,3],[-2,2]], k = 1))
