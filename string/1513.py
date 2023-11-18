# 可行的递归模拟拿不拿，但是因为10^5 会超时


class Solution:
    def numSub(self, s: str) -> int:
        def dfs(cur, i):
            nonlocal ans
            ans += 1

            if i == len(s) or s[i] == '0':
                return

            for j in range(i,len(s)):
                if s[j] == '1':
                    dfs(cur+'1', j+1)
                    return

        ans = 0
        for x in range(len(s)):
            if s[x] == '1':
                dfs('1', x+1)
        return ans

print(Solution().numSub("0110111"))
