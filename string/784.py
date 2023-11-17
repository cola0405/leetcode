from typing import List
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def dfs(cur, i):
            if i == len(s):
                return

            # 大小写
            if '0' <= s[i] <= '9':
                dfs(cur, i+1)
                ans.add(cur)
            else:
                s1 = cur[:i] + s[i].lower() + cur[i+1:]
                s2 = cur[:i] + s[i].upper() + cur[i+1:]
                ans.add(s1)
                ans.add(s2)

                dfs(s1, i+1)
                dfs(s2, i+1)

        ans = set()
        dfs(s, 0)
        return list(ans)

print(Solution().letterCasePermutation("a1b2"))