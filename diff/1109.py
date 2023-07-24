from typing import List
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0]*(n+2)
        for booking in bookings:
            first, last, amount = booking
            diff[first] += amount
            diff[last+1] -= amount
        ans = []
        p = 0
        for i in range(1, n+1):
            p += diff[i]
            ans.append(p)
        return ans

print(Solution().corpFlightBookings(bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5))
