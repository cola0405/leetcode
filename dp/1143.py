# dp[i][j] 表示 text[0:i] 与 text[0:j] 的最长公共子序列 LCS

# 有用的只有相邻的两行 -- 可使用滚动数组优化
# 进一步看是否能优化到一维： 有dp[i-1][j-1] -- 要从右往左
# 但 dp[i][j-1] 又要求从左往右，故没办法优化到一维dp

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(1,n+1):
            for j in range(1,m+1):
                # -1 是为了妥协dp的左边界
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    # 不相等时，留谁更好
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

print(Solution().longestCommonSubsequence("pmjghexybyrgzczy", "hafcdqbgncrcbihkd" ))
