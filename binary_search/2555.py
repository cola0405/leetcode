# binary search upper-bound + suffix

import bisect
from typing import List
class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        mx = [0]*(n+1)
        i = n-1
        ans = 0
        max_right = 0
        while i >= 0:
            while i-1 >= 0 and prizePositions[i] == prizePositions[i-1]:
                i -= 1
            j = bisect.bisect_right(prizePositions, prizePositions[i]+k)
            ans = max(ans, j-i+mx[j])
            max_right = max(max_right, j-i)
            mx[i] = max_right
            i -= 1
        return ans
print(Solution().maximizeWin(prizePositions = [1,1,2,2,3,3,5], k = 2))