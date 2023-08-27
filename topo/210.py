from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0] * numCourses
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

        ans = []
        while len(stack) > 0:
            idx = stack.pop()
            in_degree[idx] = -1
            for course in after_course[idx]:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    stack.append(course)
            ans.append(idx)

        return [] if max(in_degree)>0 else ans

print(Solution().findOrder(numCourses = 3, prerequisites = [[1,0],[1,2],[0,1]]))