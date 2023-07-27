# 不需要dfs出全部方案
# 贪心策略 -- 对图的next边进行排序，按从小到大顺序dfs得到的结果即为min

# dfs遍历图不进行剪枝的话，时间复杂度是O(n!)
# 数据规模是10还能暴力
# 如果数据规模上100了就肯定要剪枝、记忆搜索、贪心等手段优化了
from typing import List
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(node, order):

            # 记忆dfs
            if len(visit[node]) > 0:
                if len(order) + len(visit[node]) == n:
                    return order + visit[node]
                # 不能这么剪枝。。。可能因为visit存的不是所有状态，仍然在dfs中更新
                # elif len(order) + len(visit[node]) < n:
                #     return False

            # 所有票都使用的情况下，order中总共会有n个地方
            if len(order) == n:
                return order

            if len(g[node]) == 0:  # 没遍历完但是走到了胡同里
                # 有更长时无条件替换 -- 贪心策略，从head出发占尽可能多的点
                if len(order) > len(visit[order[0]]):
                    visit[order[0]] = order[1:]

                # 长度相等时，取字典序小的
                elif len(order) == len(visit[order[0]]):
                    visit[order[0]] = min(order[1:], visit[order[0]])
                return False
            # 遍历时remove会影响列表，所以要copy一份用来遍历
            for spot in g[node][::-1]:  # 还得判断还够不够票这么飞
                order.append(spot)  # dfs
                g[node].remove(spot)

                res = dfs(spot, order)
                if res:  # 可以一层一层直达最外层
                    return res

                order.pop()
                g[node].append(spot)  # 回溯
                g[node].sort(reverse=True)   # 回溯时需要保持列表的有序性，因为数据规模不大，直接sort了

        from collections import defaultdict
        g = defaultdict(list)
        for ticket in tickets:
            f, t = ticket
            g[f].append(t)
        n = len(tickets) + 1

        # sort
        for node in g:
            g[node].sort(reverse=True)

        visit = defaultdict(list)
        return dfs("JFK", ["JFK"])


print(Solution().findItinerary([["JFK","AAA"],["AAA","JFK"],["JFK","BBB"],["JFK","CCC"],["CCC","JFK"]]))