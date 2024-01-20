class Solution:
    def numSub(self, s: str) -> int:
        def dfs(cur, i):
            nonlocal ans
            ans += 1

            if len(cur)> 0 and i < len(s) and s[i] != '1':
                return

            # i越界 或者 s[i]不为 1时
            for x in range(i, len(s)):
                if s[x] == '1':
                    dfs(cur+'1', x+1)
                elif len(cur) > 0 and s[x] != '1':
                    return

        ans = 0
        dfs('', 0)
        return ans

print(Solution().numSub("0110111"))