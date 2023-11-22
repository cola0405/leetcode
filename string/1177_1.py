# 由于某个字母只是有或没有
# 可以把区间状态压缩到bits中

from typing import List
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        odd = []
        for ch in s:
            pass

print(Solution().canMakePaliQueries("abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]))


