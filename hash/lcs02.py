from typing import List
class Solution:
    def halfQuestions(self, questions: List[int]) -> int:
        from collections import Counter
        cnt = sorted(Counter(questions).values(), reverse=True)
        n = len(questions)//2
        for i in range(len(cnt)):
            n -= cnt[i]
            if n <= 0:
                return i+1

