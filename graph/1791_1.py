# 图的规律。。。
from typing import List
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a,b = edges[0]
        if a in edges[1]:  # 中心点必是a,b 其中一个
            return a
        return b

print(Solution().findCenter(edges = [[1,2],[5,1],[1,3],[1,4]]))
