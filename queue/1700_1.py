from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stu_count = [students.count(0), students.count(1)]
        for i in range(len(sandwiches)):
            if stu_count[sandwiches[i]] == 0:
                return sum(stu_count)
            else:
                stu_count[sandwiches[i]] -= 1
        return sum(stu_count)



print(Solution().countStudents(students = [1,1,0,0], sandwiches = [0,1,0,1]))


