# calculate a and b
# move a in O(n) and 4->3->2 can optimize to 4->2

# 4->2
# 3->1
from typing import List
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        from math import ceil
        a = 1
        b = ceil((x+y)/2)+1

        if x > y:
            x,y = y,x

        ans = [i*2 for i in range(n)][::-1]
        for i in range(1, x+1):
            origin = n-a
            cur = (x-a) + 1 + abs(y-b)

            ans[origin-1] -= 2
            ans[cur-1] += 2
            a += 1
            b -= 1
        return ans

print(Solution().countOfPairs(n = 5, x = 2, y = 4))
