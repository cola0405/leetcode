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