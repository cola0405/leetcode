# 要注意题目的前置条件
# 给的edges是一个树 + 一条额外的边
# 树有一个很重要的限制，就是除了根节点外，所有其他节点都有父节点
# 在此前提下，额外的一条边只会造成两种结果：
# ①：出现入度为2的点 -- 当发现有入度为2的点时，则看删哪一条边
# ②：成环 -- 加入当前边后成环，则表明当前边就是要返回的边

# 还有一个关心的问题就是，并查集怎么删边
# 删除当前[a,b] 构建并查集
# 如果没办法联通，则说明要返回的是另外一条边
# 如果可以联通，则说明返回的就是[a,b]

from typing import List
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        p = list(range(0, n+1))

        def find(x):
            if x == p[x]:
                return x
            p[x] = find(p[x])  # 递归更新root
            return p[x]

        def all_connected():  # 连通问题不用bfs！用并查集！
            # build graph
            from collections import defaultdict
            g = defaultdict(list)
            for a,b in edges:
                g[a].append(b)
            stack = list(g.keys())
            visit = [0]*(n+1)
            while len(stack)>0:
                top = stack.pop()
                visit[top] = 1
                stack += [node for node in g[top] if visit[node]==0]

            return True if visit.count(1) == n else False

        dst_src = dict()  # 目的地-出发地 构建dict
        for i in range(n):
            a,b = edges[i]
            if b in dst_src:  # 出现了入度为2的点
                cur_edge = edges.pop(i)

                # bfs check connection
                if all_connected():
                    return cur_edge
                else:
                    the_edge = [dst_src[b], b]  # 如果删除cur_edge不成，则取另外记录好的另外一条边返回
                    return the_edge

            elif find(b) == a:  # 利用并查集可知root来检查环
                return edges[i]
            dst_src[b] = a
            p[find(a)] = p[find(b)]

print(Solution().findRedundantDirectedConnection([[4,2],[1,5],[5,2],[5,3],[2,4]]))


