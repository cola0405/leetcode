from typing import List
from collections import deque, defaultdict
class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        if coins.count(1) == 0:
            return 0

        n = len(coins)
        in_deg = [0]*n
        g = defaultdict(list)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
            in_deg[a] += 1
            in_deg[b] += 1

        # remove the no coins leaf nodes
        flag = True
        while flag:
            flag = False
            for i in range(n):
                if coins[i] == 0 and in_deg[i] == 1:
                    flag = True
                    in_deg[i] = 0
                    for nxt in g[i]:
                        in_deg[nxt] -= 1

        # bfs for 2 times
        q = deque([i for i in range(n) if coins[i] == 1 and in_deg[i] == 1])
        already = set()
        for t in range(2):      # bfs 2 layers from coins node
            for k in range(len(q)):
                node = q.popleft()
                already.add(node)
                in_deg[node] -= 1
                for nxt in g[node]:
                    if nxt not in already:
                        in_deg[nxt] -= 1
                        already.add(nxt)
                        q.append(nxt)

        # the leaf nodes, topology sort till only one node left
        cnt = 0
        q = deque([i for i in range(n) if in_deg[i] == 1])
        while len(q) > 1:
            for k in range(len(q)):
                node = q.popleft()
                already.add(node)
                in_deg[node] = 0
                for nxt in g[node]:
                    in_deg[nxt] -= 1
                    if in_deg[nxt] == 1:
                        q.append(nxt)
            cnt += 1
        return cnt * 2

print(Solution().collectTheCoins(coins = [1,0,0,1,1,0,0,0,0,1,0,0], edges = [[0,1],[1,2],[1,3],[2,4],[4,5],[5,6],[5,7],[4,8],[7,9],[7,10],[10,11]]))

