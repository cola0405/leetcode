from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0,1]
        l = 1
        while len(res)-1 < n:
            seg1 = res[l:]
            seg2 = list(map(lambda num:num+1, res[l:]))
            res += seg1 + seg2
            l*=2
        return res[:n+1]