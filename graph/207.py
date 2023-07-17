# dfs 检查回环

# 回环和成块还是不同的
# 回环必成块
# [[1,4],[2,4],[3,1],[3,2]] 成块，但不是回环
# 所以不能用并查集，dfs吧

# 每个节点都需要进行依赖的判断
# 参数列表中带上local set 用于dfs过程中各node的local依赖检查


from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 每个节点都需要进行依赖的判断
        def dfs(node, waiting):
            if node in waiting:  # 找到了回环
                return True
            # 当前节点不构成回环，接下来检查新node的依赖
            waiting.add(node)
            for x in g[node]:
                if x in checked:  # 已经dfs检查过的节点无需再次检查
                    continue

                if dfs(x, waiting):
                    return True
                checked.add(x)  # 更新checked
            return False

        # build graph
        from collections import defaultdict
        g = defaultdict(list)
        checked = set()
        for pair in prerequisites:
            a,b = pair
            g[a].append(b)

        if len(g) > numCourses:  # 没有出现在prerequisites的可直接学
            return False

        # dfs检查回环
        for pair in prerequisites:
            a,b = pair
            if dfs(b, {a}):
                return False
        return True

print(Solution().canFinish(5,
[[1,4],[2,4],[3,1],[3,2]]))
