from typing import List
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        cnt = [0]*3000
        for a,b in logs:
            for i in range(a,b):
                cnt[i] += 1
        max_num = max(cnt)
        for year in range(1950, 2051):
            if cnt[year] == max_num:
                return year
