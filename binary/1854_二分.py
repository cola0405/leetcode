from typing import List
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        birth = [a for a,b in logs]
        death = [b for a,b in logs]
        birth.sort()
        death.sort()

        max_alive = 0
        ans = -1
        import bisect
        for i in range(len(birth)):
            year = birth[i]  # 答案必定出现在左端点
            already_born = i+1
            already_dead = bisect.bisect_right(death, year)  # 二分查找提高效率
            alive = already_born-already_dead
            if alive > max_alive:
                max_alive = alive
                ans = year
        return ans

print(Solution().maximumPopulation([[1993,1999],[2000,2010]]))


