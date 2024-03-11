# heap-iteration
from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        import heapq

        remain = len(tasks)
        cnt = Counter(tasks)
        pq = [(0,-cnt[k],k) for k in cnt]
        heapq.heapify(pq)
        ans = 0
        while remain > 0:
            t,count,task = heapq.heappop(pq)
            if t <= 0:
                count += 1
                remain -= 1
                if count != 0:
                    heapq.heappush(pq, (n+1, count, task))
            else:
                heapq.heappush(pq, (t, count, task))

            # update the whole pq
            tmp = pq[:]
            pq = []
            for item in tmp:
                t,count,task = item
                if t > 0:
                    t -= 1
                heapq.heappush(pq, (t, count, task))
            ans += 1
        return ans

print(Solution().leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], n = 1))


