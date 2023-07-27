from typing import List
class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        def learn(node):
            nonlocal ans
            if len(available) == 0:
                ans += 1
                if k-1 > 0:
                    available.append([node, k-1])
                visited[node] = 1

            elif len(available)>0:  # 用到同一天了
                for i in range(len(available)):
                    # 用并查集检查不属同块
                    if not is_parent(node, available[i][0]):
                        available[i][1] -= 1
                        user[available[i][0]].append(node)
                        if available[i][1] == 0:
                            available.pop(i)
                        visited[node] = 1
                        return
                ans += 1
                if k-1 > 0:
                    available.append([node, k - 1])
                visited[node] = 1
                return


        def dfs(node):
            if visited[node]:
                return

            if node not in g:
                learn(node)
                return

            for ref in g[node]:
                if visited[ref]:
                    continue
                dfs(ref)
            learn(node)

        def is_parent(a, b):
            if a == b:
                return True
            for node in g[a]:
                if is_parent(node, b):
                    return True
            for node in user[b]:
                if is_parent(a, node):
                    return True
            return False

        # bfs 求depth
        def get_depth():
            from collections import deque
            depth = [1]*(n+1)
            queue = deque((node, 1) for node in g.keys())
            while len(queue) > 0:
                node, cur_depth = queue.popleft()
                depth[node] = cur_depth
                for parent in g[node]:
                    queue.append((parent, cur_depth+1))
            return depth

        from collections import defaultdict
        g = defaultdict(list)
        for relation in relations:
            son, parent = relation
            g[son].append(parent)


        ans = 0
        available = []
        visited = [0]*(n+1)
        user = defaultdict(list)

        # 还得dfs得到路径长度，再根据路径长度排序+贪心，才能得到最优解。。。
        depth = get_depth()
        order = list(range(1,n+1))
        order.sort(key=lambda course: depth[course], reverse=True)

        for course in order:
            dfs(course)
        for course in range(1,n+1):
            if visited[course] == 0:
                learn(course)

        return ans

print(Solution().minNumberOfSemesters(12,
[[1,8], [1,9], [1,10], [1,11], [2,8], [2,9], [2,10], [2,11], [3,8], [3,9], [3,10], [3,11], [4,8], [4,9], [4,10], [4,11], [5,12], [6,12], [7,12]],
3))
