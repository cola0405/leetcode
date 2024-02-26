# endpoint to interval problem + scattered sliding window
from typing import List
class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)
        max_times = max(stones[-1]-stones[1]+1-(n-1), stones[-2]-stones[0]+1-(n-1))
        min_times = float('inf')
        for i in range(n):
            end = stones[i]+n  # not included
            j = i
            while j < n and stones[j] < end:    # scattered sliding window
                j += 1
            if j-i == n-1:
                if stones[j-1] == end-1:
                    min_times = min(min_times, 1)
                else:
                    min_times = min(min_times, 2)
            else:
                min_times = min(min_times, n-(j-i))
        return [min_times, max_times]

print(Solution().numMovesStonesII([100,101,104,102,103]))
