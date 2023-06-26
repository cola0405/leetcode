from typing import List
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        from collections import defaultdict
        count = defaultdict(int)
        for log in logs:
            birth, death = log
            for i in range(birth,death):
                count[i] += 1

        # 找到最早
        people = max(count.values())
        ans = float('inf')
        for year in count:
            if count[year] == people:
                ans = min(year, ans)
        return ans

print(Solution().maximumPopulation([[1993,1999],[2000,2010]]))


