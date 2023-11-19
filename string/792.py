# 暴力双指针超时
# 利用map优化匹配时的指针右移

# map 的结构如下：
# s = 'abcabc'
# {a:[0,3], b:[1,4], c[2,5]}
# 然后用二分找下一个的下标

from collections import defaultdict
from typing import List
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def sub(word):
            pass

        # build map
        nxt = defaultdict(list)
        for i in range(len(s)):
            nxt[s[i]].append(i)

        ans = 0
        for w in words:
            if sub(w):
                ans += 1
        return ans

print(Solution().numMatchingSubseq(s = "abcde", words = ["b"]))