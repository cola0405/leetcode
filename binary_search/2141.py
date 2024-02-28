from typing import List
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def fit(m):     # check whether it can support n computers run for m minutes
            total = 0
            for b in batteries:
                total += min(b, m)  # for each battery, it can be used at most min(b,m) minutes
            return m*n <= total

        low = 0
        high = sum(batteries)//n
        while low < high:
            mid = (low+high+1)//2
            if fit(mid):
                low = mid
            else:
                high = mid-1
        return low

print(Solution().maxRunTime(3,[10,10,3,5]))