# hash+set 基础题

# 判断有无公用字符也可以使用位运算 -- 26bits 然后 &运算
# 详见318_1.py

from typing import List
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        ans = 0
        for i in range(n):
            s1 = set(words[i])
            for j in range(i+1, n):
                s2 = set(words[j])
                if len(s1.intersection(s2)) == 0:
                    ans = max(ans, len(words[i])*len(words[j]))
        return ans

print(Solution().maxProduct(["eae","ea","aaf","bda","fcf","dc","ac","ce","cefde","dabae"]))
