from typing import List
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        last = 0
        for t in timeSeries:
            if t < last:
                ans += duration - (last-t)
            else:
                ans += duration
            last = t+duration
        return ans

print(Solution().findPoisonedDuration(timeSeries = [1,4], duration = 2))