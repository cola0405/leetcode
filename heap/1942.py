# heap iteration medium
from typing import List
from heapq import *
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        pq = list(range(n+1))   # empty chairs
        heapify(pq)
        leaving = []
        target_time = times[targetFriend][0]
        times.sort()
        for i in range(n):
            cur = times[i][0]
            while leaving:      # check new empty chair
                leave_time, chair = heappop(leaving)
                if leave_time > cur:
                    heappush(leaving, (leave_time, chair))
                    break
                heappush(pq, chair)
            if cur == target_time:
                return heappop(pq)
            empty_chair = heappop(pq)
            heappush(leaving, (times[i][1], empty_chair))

print(Solution().smallestChair([[33889,98676],[80071,89737],[44118,52565],[52992,84310],[78492,88209],[21695,67063],[84622,95452],[98048,98856],[98411,99433],[55333,56548],[65375,88566],[55011,62821],[48548,48656],[87396,94825],[55273,81868],[75629,91467]], 6))
