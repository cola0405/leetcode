from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            endpoint = ans[-1][1]
            if start<=endpoint:  # 判断有无重叠
                ans[-1][1] = max(end, endpoint)  # 更新endpoint
            else:
                ans.append(intervals[i])
        return ans

print(Solution().merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))