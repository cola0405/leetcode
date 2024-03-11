from typing import List
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        from sortedcontainers import SortedList
        n = len(heights)
        sl = SortedList([])
        pre = 0
        ladder_cost = 0
        for i in range(n-1):
            gap = heights[i+1] - heights[i]
            if ladders > 0:     # maintain the sum of first k cost
                if len(sl) < ladders:
                    ladder_cost += max(0, gap)
                    sl.add(gap)
                elif gap > sl[0]:
                    ladder_cost -= max(0, sl[0])
                    sl.pop(0)
                    ladder_cost += max(0, gap)
                    sl.add(gap)
            pre += max(0, gap)
            if pre - ladder_cost > bricks:   # pre[i+1] is the number of needed bricks to get to height[i+1]
                return i
        else:
            return n-1

print(Solution().furthestBuilding([1,13,1,1,13,5,11,11],10,8))