from typing import List
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0]*(n+2)
        for l, r, d in bookings:
            diff[l] += d
            if r+1 <= n:
                diff[r+1] -= d
        ans = []
        p = 0
        for i in range(1,n+1):
            p += diff[i]
            ans.append(p)
        return ans
    
    