from typing import List
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        count = [0]*100
        offset = 1950
        for log in logs:
            birth, death = log
            for i in range(birth,death):
                count[i-offset] += 1

        people = max(count)
        ans = float('inf')
        for i in range(100):
            if count[i] == people:
                year = i+offset
                ans = min(year, ans)  # 为了找到最早的年份
        return ans

print(Solution().maximumPopulation([[1993,1999],[2000,2010]]))


