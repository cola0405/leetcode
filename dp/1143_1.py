


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [0]*(m+1)

        for i in range(1,n+1):
            for j in range(1,m+1):
                # -1 是为了妥协dp的左边界
                if text1[i-1] == text2[j-1]:
                    dp[j] = min(dp[j-1] + 1, n)
                else:
                    # 不相等时，留谁更好
                    dp[j] = min(max(dp[j], dp[j-1]), n)
        return dp[-1]

print(Solution().longestCommonSubsequence("pmjghexybyrgzczy", "hafcdqbgncrcbihkd" ))
