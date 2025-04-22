'''
简单的 dp

'''

from typing import List
from collections import defaultdict
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        l = defaultdict(int)        # l[x] 表示以x结尾的最长定差子序列长度
        for x in arr:
            l[x] = max(l[x], l[x-difference] + 1)
        return max(l.values())
