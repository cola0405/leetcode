# 内向基环树 + 拓扑排序 + 深度优先搜索 + 反向图

# 内向基环树
# 题目给了一些有向边，问如何构建最大的环，或者以 x <=> y 为中点的最长链
# 圆桌的情况类似下图：
# p <- z <- x <=> y -> w -> u
# 首先如何找最大的环 —— 先使用拓扑排序去除环以外的节点，然后通过出度为 1 的特殊性通过while循环确定环的长度
# 符合题目要求的最长的链只会出现在含 x<=>y 的链中
# 所以可以找到长度为 2 的环，然后通过 dfs + 反向图往两边确定最长的链的长度（链可能存在分支，我们取其中最长的）

from typing import List
from collections import deque, defaultdict
class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        def dfs(x):
            max_len = 1
            for nxt in rg[x]:
                max_len = max(max_len, 1 + dfs(nxt))
            return max_len

        n = len(favorite)
        in_degree = [0] * n
        for i in range(n): in_degree[favorite[i]] += 1
        q = deque([i for i in range(n) if in_degree[i] == 0])
        rg = defaultdict(list)
        while q:                # 通过拓扑排序去除非环节点（只留下环）
            x = q.popleft()
            y = favorite[x]
            rg[y].append(x)     # 建立反向图 y->x
            in_degree[y] -= 1
            if in_degree[y] == 0:
                q.append(y)

        max_ring = chain_sum = 0
        for i in range(n):
            if in_degree[i] == 0: continue
            y = favorite[i]
            ring = 1
            while y != i:           # 基于题目的特殊，所有节点出度都为 1
                in_degree[y] = 0
                ring += 1
                y = favorite[y]
            if ring == 2:           # 两个节点的环是特殊情况，可以往两头构建链，这些链不矛盾，可以都插入到圆桌
                chain_sum += dfs(i) + dfs(favorite[i])
            else:                   # 其他情况，只能整环，不往外延伸链，只能取最大的环，绕着圆桌
                max_ring = max(max_ring, ring)
        return max(max_ring, chain_sum)
