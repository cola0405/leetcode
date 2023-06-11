# 并查集不依次更新每个节点的root
# 所以要看是否同源，则需要用find()去
from typing import List
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def find(x):
            if ds[x] != x:
                ds[x] = find(ds[x])  # 归root操作
            return ds[x]  # 如果当前x已经是根，则返回

        ds = list(range(n))
        for a,b in edges:
            ds[find(a)] = find(b)  # merge
        return find(source) == find(destination)  # 看是否同源，要用find()

print(Solution().validPath(n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2))

