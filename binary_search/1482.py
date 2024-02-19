# binary search + two pointers
from typing import List
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def fit(day):
            n = len(bloomDay)
            cnt = 0
            i = 0
            while i < n:
                j = i
                while j < n and j-i+1 <= k and bloomDay[j] <= day:
                    j += 1
                if j-i == k and bloomDay[i] <= day:
                    cnt += 1
                i = max(j, i+1)
            return cnt >= m

        low = min(bloomDay)
        high = max(bloomDay)
        ans = high
        while low < high:
            mid = (low+high)//2
            if fit(mid):
                high = mid
            else:
                low = mid+1
        if fit(low):
            return low
        else:
            return -1

print(Solution().minDays(bloomDay = [1,10,3,10,2], m = 3, k = 1))