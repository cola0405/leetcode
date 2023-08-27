# 离散差分 -- 空间效率更高的区间修改
from typing import List
class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        diff = defaultdict(int)
        for start, end, color in segments:  # 离散的差分
            diff[start] += color
            diff[end] -= color

        diff = sorted([k,v] for k,v in diff.items())  # 这里其实包含了后天0！
        for i in range(1, len(diff)):
            diff[i][1] += diff[i-1][1]  # 前缀和统计

        ans = []
        for i in range(len(diff)-1):
            if diff[i][1]:
                ans.append([diff[i][0], diff[i+1][0], diff[i][1]])
        return ans

print(Solution().splitPainting([[1,4,5],[1,4,7],[4,7,1],[4,7,11]]))





