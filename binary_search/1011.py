from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def fit(capacity):
            k = days
            i = 0
            for u in range(k):
                remain = capacity
                while i < n and remain > 0 and remain >= weights[i]:
                    remain -= weights[i]
                    i += 1
                if i == n:
                    return True
            return False

        n = len(weights)
        low = max(weights)
        high = sum(weights)
        while low < high:
            mid = (low+high)//2
            if fit(mid):
                high = mid
            else:
                low = mid+1
        return low