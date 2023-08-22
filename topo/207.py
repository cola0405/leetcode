# 拓扑排序

# 根据依赖关系构造：①入度表 ②依赖于它的后续课程的哈希表

# 算法过程：
# ①入度为0的课程
# ②将以来于它的后续课程入度-1
# 重复上述过程，直到没有入度为0的课程为止

from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0]*numCourses
        from collections import defaultdict
        after_course = defaultdict(list)
        for course, pre in prerequisites:
            in_degree[course] += 1
            after_course[pre].append(course)

        # 构造stack保存入度为0的课程，解决重复查找0的问题
        stack = []
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                stack.append(i)

        while len(stack)>0:
            idx = stack.pop()
            in_degree[idx] = -1
            for course in after_course[idx]:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    stack.append(course)

        return max(in_degree) < 0

print(Solution().canFinish(numCourses = 2, prerequisites = [[1,0]]))
