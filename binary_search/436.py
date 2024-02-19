import bisect
from typing import List
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        left = sorted([intervals[i][0] for i in range(n)])
        inx = {intervals[i][0]: i for i in range(n)}
        ans = []
        for start, end in intervals:
            i = bisect.bisect_left(left, end)
            if i < n and left[i] >= end:
                ans.append(inx[left[i]])
            else:
                ans.append(-1)
        return ans

print(Solution().findRightInterval([[3,4],[2,3],[1,2]]))