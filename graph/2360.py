# 内向基环树 + 拓扑排序

# 拓扑排序去除非环节点，剩下的就是环节点
# 然后再找最大环

from typing import List
from collections import deque
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        in_degree = [0]*n
        for i in range(n):      # 因为存在无出度的 -1 节点，所以需要特殊处理一下
            if edges[i] >= 0: in_degree[edges[i]] += 1
        q = deque([i for i in range(n) if in_degree[i] == 0])
        while q:                # 拓扑排序去除非环节点
            x = q.popleft()
            y = edges[x]
            if y == -1: continue
            in_degree[y] -= 1
            if in_degree[y] == 0:
                q.append(y)
        ans = 0
        for i in range(n):
            if in_degree[i] <= 0: continue
            y = edges[i]
            ring = 1
            while y != i:
                in_degree[y] = 0
                ring += 1
                y = edges[y]
            ans = max(ans, ring)
        return ans if ans >= 2 else -1      # 不存在 x->y 的非环情况，因为拓扑完了，剩下的都是环

print(Solution().longestCycle([1,0]))
