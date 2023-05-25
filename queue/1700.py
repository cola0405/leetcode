from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        from collections import deque
        students = deque(students)
        sandwiches = deque(sandwiches)
        count = [students.count(0), students.count(1)]
        # keep while there still got two kind of likes
        while (count[0] != len(students) and count[1] != len(students)) \
            or (len(students)>0 and len(sandwiches)>0 and students[0] == sandwiches[0]):
            if students[0] == sandwiches[0]:
                sandwiches.popleft()
                count[students.popleft()] -= 1
            else:
                students.append(students.popleft())
        return len(students)

print(Solution().countStudents(students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]))


