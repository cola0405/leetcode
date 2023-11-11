# 递归的剪枝优化
# 600 的数据范围，也是可以剪枝递归AC的

from typing import List
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def dfs(i, count, zero, one):  # 到i时选了count个字符串，zero和one的个数
            if zero > m or one > n:
                return 0
            if i == len(strs):
                return count
            if (i,count, zero,one) in already:
                return 0

            zero_count = strs[i].count('0')
            one_count = strs[i].count('1')
            already.add((i,count,zero,one))  # 表示这种情况，以后不用再递归下去

            return max(dfs(i+1, count+1, zero+zero_count,one+one_count),
                       dfs(i+1, count, zero, one))

        already = set()
        return dfs(0, 0, 0, 0)

print(Solution().findMaxForm(["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"], m = 9, n = 80))