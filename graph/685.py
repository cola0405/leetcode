# 要注意题目的前置条件
# 给的edges是一个树 + 一条额外的边
# 树有一个很重要的限制，就是除了根节点外，所有其他节点都有父节点
# 在此前提下，额外的一条边只会造成两种结果：
# ①：出现入度为2的点 -- 当发现有入度为2的点时，则看删哪一条边，答案必定在这两条边中
# ②：成环 -- 加入当前边后成环，则表明要删除的边就在构成环的那几条边中(无法马上定)
# 又成环的任一条边删除后都可成树，但是题目要求输出最右，则保存成环的最后一条边

# 代码的逻辑就是：先遍历找入度为2的，如果没有则返回成环的最后一条边


# 还有一个关心的问题就是，并查集怎么删边
# 删除当前[a,b] 构建并查集
# 如果没办法联通，则说明要返回的是另外一条边
# 如果可以联通，则说明返回的就是[a,b]

from typing import List
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        p0 = list(range(0, n+1))  # used for cycle check

        def find(p, x):
            if x == p[x]:
                return x
            p[x] = find(p, p[x])  # 递归更新root
            return p[x]

        def all_connected():  # 连通问题不用bfs！用并查集！
            p1 = list(range(0, n+1))
            for a, b in edges:
                p1[find(p1, b)] = p1[find(p1,a)]
            root = {find(p1,node) for node in range(1,n+1)}  # get root
            return True if len(root)==1 else False  # 唯一root则是树

        edge_do_cycle = None
        dst_src = dict()  # 目的地-出发地 构建dict
        for i in range(n):
            a,b = edges[i]
            if b in dst_src:  # 出现了入度为2的点
                cur_edge = edges.pop(i)  # 尝试删除，然后构建并查集看连通性

                # 并查集 check connection
                if all_connected():
                    return cur_edge
                else:
                    the_edge = [dst_src[b], b]  # 如果删除cur_edge不成，则取另外记录好的另外一条边返回
                    return the_edge

            # 这里是变种并查集，find返回的是当前节点最远走到哪
            elif find(p0, b) == a:  # 利用并查集可知root来检查环
                edge_do_cycle = edges[i]
            dst_src[b] = a
            p0[find(p0,a)] = p0[find(p0,b)]
        return edge_do_cycle


print(Solution().findRedundantDirectedConnection([[3,4],[4,1],[1,2],[2,3],[5,1]]))


