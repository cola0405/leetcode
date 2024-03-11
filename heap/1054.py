# greedy + select maximum every time
from typing import List
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        from collections import Counter
        import heapq
        cnt = Counter(barcodes)
        pq = [(-cnt[num], num) for num in cnt]
        heapq.heapify(pq)
        ans = []
        while len(ans) < len(barcodes):
            count, num = heapq.heappop(pq)
            count *= -1
            if len(ans) == 0 or num != ans[-1]:
                ans.append(num)
                if count-1 > 0:
                    heapq.heappush(pq, (-(count-1), num))
            else:
                count1, num1 = heapq.heappop(pq)
                count1 *= -1
                ans.append(num1)
                if count-1 > 0:
                    heapq.heappush(pq, (-(count1-1), num1))
                heapq.heappush(pq, (-count, num))
        return ans

print(Solution().rearrangeBarcodes( [1,1,1,1,2,2,3,3]))

