# 根据 s1 s2 求奇数数量的时候有优化
# 直接异或，然后统计 1 的数量

from typing import List
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        status = [0]
        for ch in s:
            # 表明了各个字母的奇偶状态变化，0:偶数, 1:奇数
            bits = status[-1] ^ (1 << (ord(ch) - 97))
            status.append(bits)

        ans = []
        for left, right, k in queries:
            # 直接异或，然后统计 1 的数量
            bits = status[left] ^ status[right+1]
            odd = 0
            while bits > 0:
                bits = bits&(bits-1)
                odd += 1

            ans.append(odd-2*k <= 1)

        return ans


print(Solution().canMakePaliQueries("abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]))


