# 序列dp


from typing import List
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        s = set(words)
        ans = []
        for word in words:
            n = len(word)
            dp = [0]*(n+1)  # dp[i] 表示从右往左长度为1
            dp[0] = 1  # i-len(cur)==0 表示当前这个片段有1种构造方法
            for i in range(1,n+1):  # 从1到n长度，构造dp
                for j in range(i):  # 以i结尾的往前各种长度的片段
                    cur = word[j:i]
                    if cur in s:
                        dp[i] += dp[i-len(cur)]
            if dp[-1]>1:
                ans.append(word)
        return ans

print(Solution().findAllConcatenatedWordsInADict(["a","b","ab","abc"]))
