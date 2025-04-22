'''
题目大意：
我们可以选择某些区间来获取最大收益（要求区间不能重叠）

思路：
思考 dp状态时，我们会遇到一个问题，无法获取之前区间的选择情况（不可能暴力记录）
那我们状态转移的关键点在哪呢？
如果我们以房屋作为 dp的对象，dp[i] 表示到第 i个屋子的最大收益
状态转移方程：dp[i] = max(dp[start] + gold)
start 是以 i作为区间末尾的区间起点，可能有多个，我们在其中取最大值
通过转化研究对象以及区间的 dp转移，我们就可以不顾之前区间的选择情况了


'''


from typing import List
class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        from collections import defaultdict
        offset = 1
        end = defaultdict(list)             # 记录以 i 为结尾的区间
        for i in range(len(offers)):
            end[offers[i][1] + offset].append(i)        # 因为涉及到 [i-1] 又题目房屋从 0开始算，所以需要做一个偏移
        dp = [0] * (n+1)
        for i in range(1, n+1):
            dp[i] = dp[i-1]     # 不卖当前屋子
            for j in end[i]:    # 遍历以 i为结尾的区间
                a,b,gold = offers[j]
                a += offset
                b += offset
                dp[i] = max(dp[i], dp[a-1] + gold)      # 注意要取的是 a前一位的 dp状态
        return dp[-1]

print(Solution().maximizeTheProfit(n = 5, offers = [[0,0,1],[0,2,10],[1,3,2]]))
