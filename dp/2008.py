'''
参考 2830


'''

from typing import List
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        from collections import defaultdict
        end = defaultdict(list)
        for i in range(len(rides)):
            end[rides[i][1]].append(i)

        dp = [0]*(n+1)
        for i in range(1,n+1):
            dp[i] = dp[i-1]
            for j in end[i]:
                earn = (rides[j][1]-rides[j][0]) + rides[j][2]
                dp[i] = max(dp[i],dp[rides[j][0]] + earn)       # 因为可以在同一个地点放下乘客、接新的乘客，所以不用 -1，直接 rides[j][0]就可以
        return dp[-1]

print(Solution().maxTaxiEarnings(20, [[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]]))