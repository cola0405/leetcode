from typing import List
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        from collections import defaultdict
        path = defaultdict(int)
        for a,b in edges:
            path[a] += 1
            path[b] += 1

        for node in path:
            if path[node] == len(path)-1:
                return node

print(Solution().findCenter(edges = [[1,2],[5,1],[1,3],[1,4]]))
