from typing import List
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        ans = [0]*(n+1)
        for a in range(1,n+1):
            for b in range(1,n+1):
                if a == b:
                    continue
                d1 = abs(a-b)
                d2 = abs(a-x) + abs(b-y) + 1
                d3 = abs(a-y) + abs(b-x) + 1
                ans[min(d1,d2,d3)] += 1
        return ans[1:]
