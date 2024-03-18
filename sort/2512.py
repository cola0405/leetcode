from typing import List
class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        from collections import defaultdict
        cnt = defaultdict(int)
        for stu_id in student_id:
            cnt[stu_id] = 0
        positive = set(positive_feedback)
        negative = set(negative_feedback)
        for i in range(len(student_id)):
            words = report[i].split()
            stu_id = student_id[i]
            for word in words:
                if word in positive:
                    cnt[stu_id] += 3
                elif word in negative:
                    cnt[stu_id] -= 1
        score = [(cnt[stu_id], -stu_id) for stu_id in cnt]
        score.sort(reverse=True)
        return [-item[1] for item in score[:k]]

print(Solution().topStudents(positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is not studious","the student is smart"], student_id = [1,2], k = 2))


