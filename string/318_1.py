# hash+set 基础题

# 太多重复的set构造，可优化

from typing import List
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def to_bits(s):
            res = 0
            for ch in s:
                res |= 1<<(ord(ch)-ord('a'))
            return res

        n = len(words)
        ans = 0

        sheet = [to_bits(word) for word in words]

        for i in range(n):
            for j in range(i+1, n):
                if sheet[i]&sheet[j] == 0:
                    ans = max(ans, len(words[i])*len(words[j]))
        return ans

print(Solution().maxProduct(["eae","ea","aaf","bda","fcf","dc","ac","ce","cefde","dabae"]))
