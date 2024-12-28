# dijastra
# 10^5 不可能是构建完整 nxn 的图，肯定应该是离散的
# 那我们就不能往四个方向去 dijastra, 而是得结合 special roads 去走
# 因为 len(sr) <= 200 所以不难想到，我们在 dijastra 的过程中去尝试走到每一个 special road 的起点

from typing import List
from collections import defaultdict
import heapq

class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        q = [(0, start[0], start[1])]
        sr = defaultdict(list)     # special road
        min_dis = defaultdict(lambda: float('inf'))    # min_dis
        for x1,y1,x2,y2,c in specialRoads:
            sr[(x1,y1)].append((x2,y2,c))
            heapq.heappush(q, (abs(start[0]-x1) + abs(start[1]-y1), x1, y1))
        while q:
            cost,x,y = heapq.heappop(q)
            if cost > min_dis[(x,y)]: continue
            min_dis[(x,y)] = cost   # 这里不需要额外计算 dis 取最小值的原因也是因为 dijastra, 因为到其父节点的已经确定是最短距离了
            # go through special road, update min_dis
            if (x,y) in sr:
                for x1,y1,c in sr[(x,y)]:
                    if cost+c < min(min_dis[(x1,y1)], abs(start[0]-x1)+abs(start[1]-y1)):
                        heapq.heappush(q, (cost+c, x1, y1))
                sr.pop((x,y))       # dijastra 的一个特点就是每个点只会被访问一次

            # try go to start point of special road
            for x1,y1 in sr:
                d = abs(x-x1) + abs(y-y1) + min_dis[(x,y)]
                if d < min(min_dis[(x1,y1)], abs(start[0]-x1)+abs(start[1]-y1)):
                    heapq.heappush(q, (d, x1, y1))
        # try every min_dis to target
        ans = float('inf')
        for x,y in min_dis:
            ans = min(ans, min_dis[(x,y)] + abs(x-target[0])+abs(y-target[1]))
        return ans

print(Solution().minimumCost(start = [1,1], target = [9,9], specialRoads = [[2,4,9,2,1],[4,8,4,4,4],[5,9,9,9,1],[3,9,7,9,3]]))