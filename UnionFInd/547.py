# 并查集经典算法

from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(node):
            if node == p[node]:
                return node
            p[node] = find(p[node])
            return p[node]

        n = len(isConnected)
        p = list(range(n))
        ans = n
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and find(i) != find(j):
                    # 这里只是把root的父节点给改了
                    # root之下的都还没更新，可以通过find()更新
                    # 但如果循环到此就结束的话，那会有部分节点的root不是直接关联
                    # 用set+len得到块数量的方法会有问题
                    # 用ans-- 的方法合理，合并一块少一块
                    p[find(j)] = p[find(i)]
                    ans -= 1  # set去长度为什么不行应该是有一些节点没更新
        return ans

print(Solution().findCircleNum([[1,1,1,0,1,1,1,0,0,0],[1,1,0,0,0,0,0,1,0,0],[1,0,1,0,0,0,0,0,0,0],[0,0,0,1,1,0,0,0,1,0],[1,0,0,1,1,0,0,0,0,0],[1,0,0,0,0,1,0,0,0,0],[1,0,0,0,0,0,1,0,1,0],[0,1,0,0,0,0,0,1,0,1],[0,0,0,1,0,0,1,0,1,1],[0,0,0,0,0,0,0,1,1,1]]))

