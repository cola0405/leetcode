# 问题转化 -- max(min)问题
# 怎么找min -- 双指针移动得到[i]和[i-1]

from typing import List
class Solution:
    def findRadius(self, houses: List[int], heaters) -> int:
        houses.sort()
        heaters.sort()
        heaters.insert(0, float('-inf'))
        heaters.append(float('inf'))

        ans = 0
        i = 0
        for house in houses:
            # 找到刚好大于house的heater
            while i<len(heaters) and heaters[i]<house:
                i += 1
            left_gap = house - heaters[i-1]  # 那么[i-1]就是刚好小于house的heater
            right_gap = heaters[i] - house
            ans = max(min(left_gap, right_gap), ans)  # max(min)问题
        return ans


print(Solution().findRadius(houses = [1,5], heaters = [10]))

