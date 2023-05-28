from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda item: item[0])
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            # 合并（重叠）的情况：①前包后②后包前③叠
            if ans[-1][1] >= intervals[i][1] or intervals[i][0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
            else:
                ans.append(intervals[i])
        return ans

print(Solution().merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))