from typing import List
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n == 1:
            return True
        reachable = {source,}  # reachable from source
        pre_len = len(reachable)
        while True:  # 有点像广度优先
            for a,b in edges:
                if a in reachable:
                    reachable.add(b)
                elif b in reachable:
                    reachable.add(a)
                if destination in reachable:
                    return True
            # 没有新增的reachable节点了
            if len(reachable) == pre_len:
                return False
            pre_len = len(reachable)


print(Solution().validPath(n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5))


