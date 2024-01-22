# 可凑齐的面值 + greedy

# 解决这道题需要有一个结论：
# 当前可达范围 [0,s] 若有 coins[i] 加入
# 则可达范围会变化成 [coins[i], s+coins[i]]

# 如果新范围的下边界 coins[i] <= s+1 那么可达范围可以顺利扩展为 [0, s+coins[i]]

# 如果 coins[i] > s 则表示中间会有一些数字没覆盖到
# 最左边的数字为 s+1 —— 这个就是我们当前贪心必须要额外插入的数字
# 插入 s+1 后，可达范围会变化为 [0, s+(s+1)]

# 我们贪心要干的事情就是 —— 找到这些必须要额外插入的数字

from typing import List
class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        i,s = 0,0   # [0,s] 表示当前能够取到的数
        ans = 0
        while s < target:
            if i < len(coins) and coins[i] <= s+1:
                s += coins[i]   # 可以顺利拼接新范围，更新右端点
                i += 1
            else:            # 有数字没被覆盖 —— s+1是最左，必须被插入的数字
                s += s+1    # 插入 s+1 后，更新右端点
                ans += 1
        return ans


print(Solution().minimumAddedCoins([1,4,10], 19))