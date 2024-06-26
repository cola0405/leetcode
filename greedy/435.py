from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        top = intervals[0][1]
        ans = -1
        for start,end in intervals:
            if start < top:
                top = min(top, end)
                ans += 1
            else:
                top = end
        return ans

print(Solution().eraseOverlapIntervals( [[0,2],[1,3],[2,4],[3,5],[4,6]]))

