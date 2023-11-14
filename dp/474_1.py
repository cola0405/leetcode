from functools import cache
from typing import List
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @cache
        def dfs(i, count, zero, one):  # 到i时选了count个字符串，zero和one的个数
            if zero > m or one > n:
                return 0
            if i == len(strs):
                return count

            zero_count = strs[i].count('0')
            one_count = strs[i].count('1')

            return max(dfs(i+1, count+1, zero+zero_count,one+one_count),
                       dfs(i+1, count, zero, one))

        return dfs(0, 0, 0, 0)

print(Solution().findMaxForm(["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"], m = 9, n = 80))