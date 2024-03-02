import bisect
from typing import List
class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        rooms = [[s,i] for i,s in rooms]
        rooms.sort()
        n = len(rooms)
        for pre, s in queries:
            low = 0
            high = n-1
            while low < high:
                mid = (low+high)//2
                if rooms[mid][0] >= s:
                    high = mid
                else:
                    low = mid+1
            high = n-1
            while low < high:
                mid = (low+high)//2
                if rooms[mid][1] >= pre:
                    pass
                    

print(Solution().closestRoom(rooms = [[2,2],[1,2],[3,2]], queries = [[3,1],[3,3],[5,2]]))