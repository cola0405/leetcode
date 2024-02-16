# binary search + greedy

#
from typing import List
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        from math import sqrt
        def fit(t):     # check whether it can fix n car within time t
            cnt = 0
            for r in ranks:
                cnt += int(sqrt(t/r))
            return cnt >= cars

        low = 1
        high = int(1e18)
        while low < high:
            mid = (low+high)//2
            if fit(mid):
                high = mid
            else:
                low = mid+1
        return low
