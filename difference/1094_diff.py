from typing import List
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0]*1001
        for trip in trips:
            amount, start, end = trip
            diff[start] += amount
            diff[end] -= amount
        max_count = 0
        count = 0
        for i in range(len(diff)):
            count += diff[i]
            max_count = max(count, max_count)
        return capacity >= max_count

print(Solution().carPooling([[2,1,5],[3,3,7]],
5))