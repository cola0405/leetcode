from typing import List
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        from math import ceil
        def fit(speed):
            t = 0
            for i in range(len(dist)-1):
                t = ceil(t + dist[i]/speed)
            return t+dist[-1]/speed <= hour

        low = 1
        high = int(1e7)+1
        while low < high:
            mid = (low+high)//2
            if fit(mid):
                high = mid
            else:
                low = mid+1
        if high == int(1e7)+1:
            return -1
        return low

print(Solution().minSpeedOnTime(dist = [1,3,2], hour = 1.9))