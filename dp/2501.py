from typing import List
from collections import defaultdict
from math import sqrt
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        l = defaultdict(int)        # l[x] 表示以x结尾的最长方波长度
        for x in nums:
            s = sqrt(x)
            if s*10%10 == 0:
                l[x] = max(l[x], l[int(s)] + 1)
            if l[x] == 0:
                l[x] = 1
        ans = max(l.values())
        return ans if ans > 1 else -1

print(Solution().longestSquareStreak([4,3,6,16,8,2]))