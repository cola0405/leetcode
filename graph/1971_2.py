from typing import List
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        from collections import defaultdict
        from collections import deque

        if n == 1:
            return True

        path = defaultdict(list)
        for edge in edges:
            a, b = edge
            path[a].append(b)
            path[b].append(a)

        visit = set()

        # 非递归也没办法解决1e5
        queue = deque(path[source])
        while len(queue)>0:
            if queue[0] == destination:
                return True
            visit.add(queue[0])  # 剪枝
            for p in path[queue[0]]:
                if p not in visit:
                    queue.append(p)
            queue.popleft()
        return False

print(Solution().validPath(n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5))


