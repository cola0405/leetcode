from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        ans = ''
        j = 0
        while j<len(strs[0]):
            for i in range(1, len(strs)):
                if len(strs[i])<=j or strs[0][j] != strs[i][j]:
                    break
            else:
                ans += strs[i][j]
                j += 1
                continue
            break
        return ans

print(Solution().longestCommonPrefix(["",""]))
