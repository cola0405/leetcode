from typing import List
class Solution:
    def minimumSwitchingTimes(self, source: List[List[int]], target: List[List[int]]) -> int:
        from collections import defaultdict
        cnt1 = defaultdict(int)
        cnt2 = defaultdict(int)

        for i in range(len(source)):
            for j in range(len(source[0])):
                cnt1[source[i][j]] += 1
                cnt2[target[i][j]] += 1

        ans = 0
        for color in cnt1:  # only consider the extra part
            if cnt1[color] > cnt2[color]:
                ans += cnt1[color] - cnt2[color]
        return abs(ans)