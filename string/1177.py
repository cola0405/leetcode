# 前缀和
# 可任意排列顺序，则回文串检测只与数量有关系
# 只要 odd<=1 即可

# 又题目存在变化，需要找到规律：变换一次可以消除两个odd
# 这里注意：只要某字母数量是odd，变换任意一个字母，他就变成even了
# 再变换的目标是另外一个odd，则可以 “一次变换消除两个odd”

# 所以解题的关键在于，需要一种快速统计区间和的方法 -- 前缀和

from typing import List
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        from collections import defaultdict
        # build prefix sum
        count = defaultdict(list)
        for i in range(26):
            ch = chr(97+i)
            count[ch].append(0)
            for j in range(len(s)):
                if s[j] == ch:
                    count[ch].append(count[ch][-1]+1)
                else:
                    count[ch].append(count[ch][-1])

        ans = []
        for left, right, k in queries:
            odd = 0
            for i in range(26):
                ch = chr(97+i)
                amount = count[ch][right+1] - count[ch][left]
                if amount%2 != 0:
                    odd += 1
            ans.append(odd == 1 or odd - 2*k <= 1)
        return ans

print(Solution().canMakePaliQueries("abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]))


