from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        p = list(range(0, n+1))

        def find(x):
            if x == p[x]:
                return x
            p[x] = find(p[x])  # 递归更新root
            return p[x]

        for i in range(n):
            a,b = edges[i]
            if find(a) == find(b):  # compare the root
                return edges[i]
            p[find(a)] = p[find(b)]  # merge the root is enough


print(Solution().findRedundantConnection(edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]))

