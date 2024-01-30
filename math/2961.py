# 带余除法 —— 只取后x位

from typing import List
class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        ans = []
        for inx in range(len(variables)):
            a,b,c,m = variables[inx]
            num = a
            res = 1
            for i in range(b):
                res *= num
                res %= 10

            num = res
            res = 1
            for i in range(c):
                res *= num
                res %= m

            if res == target:
                ans.append(inx)
        return ans

print(Solution().getGoodIndices([[2,3,3,10],[3,3,3,1],[6,1,1,4]], target = 2))
