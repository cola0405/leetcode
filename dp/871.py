'''

经典二维 dp
dp[i][j] 表示走完第 i个加油站，加了 j次油的最大油量
这里要注意的就是不仅仅要判断加/不加油，还要考虑是否能走到 i


'''

from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)
        if n==0: return -1 if startFuel<target else 0
        dp = [[-1]*(n+1) for _ in range(n+1)]  # dp[i][j] 表示走完第 i个加油站，加了 j次油的最大油量
        dp[0][0] = startFuel
        pre_pos = 0  # 记录上一个加油站的位置
        for i in range(1, n+1):
            dis = stations[i-1][0]-pre_pos
            pre_pos = stations[i-1][0]
            if dp[i-1][i-1]<dis: return -1  # 每个站都加油还是到不了下一个加油站
            for j in range(i):  # 把之前加了[0,i-1]次油的状态都走一遍
                remain = dp[i-1][j]-dis  # 加了[j-1]次油，走到第 i个加油站，剩余油量为 remain
                if remain<0: continue  # 到不了第 i个加油站的就不考虑加油了
                dp[i][j] = max(dp[i][j], remain)  # 不加油
                dp[i][j+1] = max(dp[i][j+1], remain+stations[i-1][1])  # 在第 i个站加油

        for cnt in range(n+1):  # 找到达到第 n个加油站，而且油量够走到目标位置的最少加油次数
            if dp[n][cnt]>=(target-stations[-1][0]): return cnt
        return -1


print(Solution().minRefuelStops(target=999, startFuel=1000, stations=[[5, 100], [997, 100], [998, 100]]))
