from typing import List
class Solution:
    def temperatureTrend(self, temperatureA: List[int], temperatureB: List[int]) -> int:
        def get_flags(t):
            flags = [0]*n
            for i in range(n-1):
                if t[i] > t[i+1]:
                    flags[i] = -1
                elif t[i] < t[i+1]:
                    flags[i] = 1
                else:
                    flags[i] = 0
            return flags

        n = len(temperatureA)
        f1 = get_flags(temperatureA)
        f2 = get_flags(temperatureB)

        ans = 0
        for i in range(n):
            for j in range(i,n):
                if f1[j] != f2[j]:
                    ans = max(ans, j-i)
                    break
            else:
                ans = max(ans, j-i)
        return ans

print(Solution().temperatureTrend(temperatureA = [21,18,18,18,31], temperatureB = [34,32,16,16,17]))


