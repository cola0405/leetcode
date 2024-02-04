# greedy + priority queue

# sort first then focus the right
# if the current groups can take the new interval, just take it
# if not, create a new group -- greedy
import heapq
from typing import List
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        pq = []
        for l,r in intervals:
            if len(pq) == 0:
                heapq.heappush(pq, r)
            else:
                top = heapq.heappop(pq)
                if l <= top:
                    heapq.heappush(pq, top)
                heapq.heappush(pq, r)
        return len(pq)

print(Solution().minGroups([[5,10],[6,8],[1,5],[2,3],[1,10]]))