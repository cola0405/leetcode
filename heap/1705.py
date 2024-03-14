# heap iteration + greedy
from typing import List
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        import heapq
        pq = []     # sort by rot_day -- greedy eat the nearly rotted apple first
        n = len(apples)
        ans = 0
        for i in range(n):
            heapq.heappush(pq, (i+days[i], apples[i]))
            while len(pq) > 0:
                rot_day, number = heapq.heappop(pq)
                if rot_day > i and number > 0:
                    ans += 1
                    if number > 1:
                        heapq.heappush(pq, (rot_day, number-1))
                    break
        i = n
        while len(pq) > 0:
            while len(pq) > 0:
                rot_day, number = heapq.heappop(pq)
                if rot_day > i and number > 0:
                    ans += 1
                    if number > 1:
                        heapq.heappush(pq, (rot_day, number-1))
                    break
            i += 1
        return ans

print(Solution().eatenApples([1,2,3,5,2], [3,2,1,4,2]))