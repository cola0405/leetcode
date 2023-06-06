from typing import List
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visit = {0}
        stack = rooms[0][:]
        while len(stack)>0:
            top = stack.pop()
            visit.add(top)
            stack += [room for room in rooms[top] if room not in visit]
        if len(visit) == n:
            return True
        return False

print(Solution().canVisitAllRooms(rooms = [[1,3],[3,0,1],[2],[0]]))

