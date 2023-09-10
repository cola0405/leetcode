# 序列dp

# 详细解析参考472
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                seg = s[j:i]
                if seg in words:
                    dp[i] += dp[i-len(seg)]

        if dp[-1]>=1:  # 在这里能达到即可所以>=1，472是要求必须得由其他单词组成，所以要>1
            return True
        return False

print(Solution().wordBreak(s = "leetcode", wordDict = ["leet", "code"]))
