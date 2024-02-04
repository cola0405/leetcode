from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        from math import ceil
        def fit(k):
            t = 0
            for p in piles:
                t += ceil(p/k)
                if t > h:
                    return False
            return True

        low = 1
        high = max(piles)
        while low < high:
            mid = (low+high)//2
            if fit(mid):
                high = mid
            else:
                low = mid+1
        return low