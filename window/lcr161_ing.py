# not sliding window
from typing import List
class Solution:
    def maxSales(self, sales: List[int]) -> int:
        n = len(sales)
        i = 0
        window = sales[0]
        ans = sales[0]
        for j in range(1,n):
            window += sales[j]
            ans = max(ans, window)
            while i < n and sales[i] < 0 or i < j and (window <= 0 or j == n-1):
                window -= sales[i]
                ans = max(ans, window)
                i += 1
        return ans

print(Solution().maxSales([-1,2,2,-3]))

