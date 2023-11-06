# 最小的时间差
# 要不是顺时针数，就是逆时针数

# 顺时针 -- 那肯定出现在相邻的两个时间点上
# 逆时针 -- 那就肯定是时间间隔最大的两个时间点，然后值为1440-gap

from typing import List
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def get_time(s):
            a, b = map(int, s.split(':'))
            return a*60 + b

        t = list(map(get_time, timePoints))
        t.sort()

        max_gap = max(t) - min(t)
        min_gap = float('inf')
        for i in range(1, len(t)):
            min_gap = min(min_gap, t[i]-t[i-1])
        return min(1440-max_gap, min_gap)



print(Solution().findMinDifference(timePoints = ["12:12","12:13","00:12","00:13"]))
