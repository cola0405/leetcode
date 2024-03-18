# customize the queries + heap
# make sure to push the points in heap after the b of [a,b]
from typing import List
from heapq import *
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)
        left = [[] for _ in range(n)]   # record the previous point which is greater than cur
        ans = [-1] * len(queries)
        for i in range(len(queries)):
            a,b = queries[i]
            if a > b:
                a,b = b,a
            if a == b or heights[a] < heights[b]:
                ans[i] = b
            else:               # the target is greater than heights[a] and after "b"
                left[b].append((heights[a], i))     # only focus on the greater element heights[a]

        pq = []
        for i in range(n):
            while pq and pq[0][0] < heights[i]:
                ans[heappop(pq)[1]] = i
            for item in left[i]:    # push the points in heap after the b of [a,b]
                heappush(pq, item)
        return ans

print(Solution().leftmostBuildingQueries(heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]))