from typing import List
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[
        bool]:
        def dfs(x):
            if vis[x]: return
            vis[x] = 1
            pre[cur_node].add(x)
            for nxt in g[x]: dfs(nxt)

        from collections import defaultdict
        g = defaultdict(list)
        pre = defaultdict(set)

        # 构建图
        for a,b in prerequisites: g[b].append(a)

        # 往前置节点 dfs
        for node in range(numCourses):
            vis = [0]*numCourses
            cur_node = node
            dfs(node)
        ans = []
        for u,v in queries: ans.append(u in pre[v])
        return ans


