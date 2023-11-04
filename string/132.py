# 后效性不是直观上观察到的
# dp 不关心之前的状态是怎么达到的，只记录数值
# 所以只要题目没限制，选了a就不能选b
# 那就可以dp

# 直观上的观察只能判定是否可以使用贪心

# 快速构造 回文查询sheet
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        if n == 1: return 0

        # fast build of palindrome
        # p[i][j] 为 True 表示 [i,j] 为回文串
        # 构造的时候必须让i从大到小构建，才能实现递推
        p = [[True]*n for _ in range(n)]
        for i in range(n-1)[::-1]:
            for j in range(i+1, n):
                # 中间回文+两端相等 -> 新回文串成立
                if s[i] == s[j] and p[i+1][j-1]:
                    p[i][j] = True
                else:
                    p[i][j] = False

        # dp[i] 表示长度为i+1的字符串的最小切割次数
        dp = [float('inf')]*n
        dp[0] = 0
        for i in range(1,n):
            if p[0][i]:
                dp[i] = 0
            else:
                # 如果[j,i]为回文串，则dp[i] = min(dp[i], dp[j-1]+1)
                for j in range(1,i+1):
                    if p[j][i]:
                        dp[i] = min(dp[i], dp[j-1]+1)
        return dp[-1]

print(Solution().minCut("cabababcbc"))