from typing import List
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        count = [0]*1001
        for trip in trips:
            amount, start, end = trip
            for i in range(start, end):
                count[i] += amount
        return capacity >= max(count)

print(Solution().carPooling(trips = [[2,1,5],[3,3,7]], capacity = 5))