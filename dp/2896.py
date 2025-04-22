'''
一维线性 dp

1. 这道题需要对原始数据进行预处理，得到数组 p，存储需要进行反转的所有位置
2. 这道题的状态转移方程比较特殊，不是直接应用题目给的条件进行转移

转移分两种情况：
进行操作 1：处理第 i位，则后续就会有某一位可以免费进行反转，这里用 free来做标记
进行操作 2：多次处理相邻项，从而反转 p[i-1]和 p[i]

'''

class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        p = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                p.append(i)
        if len(p) == 0: return 0
        if len(p)%2 == 1: return -1          # 一定是偶数个反转才有可能完成
        dp = [float('inf')] * (len(p)+1)     # 处理 [0,i]不同需要的最少操作次数
        dp[0] = 0
        dp[1] = x                         # 主要是为了应付 dp[i-2]
        free = 1                          # 下一个反转可以免费进行
        for i in range(2, len(p)+1):
            if free:
                dp[i] = min(dp[i-1], dp[i-2] + abs(p[i-1]-p[i-2]))
                free = 0
            else:
                dp[i] = min(dp[i-1] + x, dp[i-2] + abs(p[i-1]-p[i-2]))      # p数组有 offset
                free = 1
        return int(dp[-1])

print(Solution().minOperations(s1 = "1100011000", s2 = "0101001010", x = 2))