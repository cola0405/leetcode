# 2 dimensional difference for interval update
from typing import List
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0]*(n+1) for u in range(n)]
        for x1,y1,x2,y2 in queries:
            for i in range(x1, x2+1):
                diff[i][y1] += 1
                diff[i][y2+1] -= 1
        ans = []
        for i in range(n):
            line = [diff[i][0]]
            for j in range(1,n):
                line.append(line[-1] + diff[i][j])
            ans.append(line)
        return ans

print(Solution().rangeAddQueries(n = 3, queries = [[1,1,2,2],[0,0,1,1]]))
