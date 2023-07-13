# 贪心
# 把尽可能大的字符串往前面堆
from typing import List
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 交换位置之后能更大，则说明s2要比s1在当前规则下更大
        # 把大的字符串往前面堆，则组成的数字最大
        def cmp(s1, s2):
            return s1+s2 < s2+s1

        s = list(map(str, nums))
        for i in range(len(s)-1):
            max_idx = i
            for j in range(i+1, len(s)):
                if cmp(s[max_idx], s[j]):
                    max_idx = j
            s[i], s[max_idx] = s[max_idx], s[i]

        while len(s)>1 and s[0] == '0':
            s.pop(0)
        return ''.join(s)

print(Solution().largestNumber([0,0]))
