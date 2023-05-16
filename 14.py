from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = 2000
        for i in strs:
            if len(i) < min_len:
                min_len = len(i)
        if min_len == 0:
            return ""
        i = 0
        common = ""
        while i < min_len:
            l = len(common)
            for index in range(len(strs)-1):
                if strs[index][i] != strs[index+1][i]:
                    break
            else:
                common += strs[0][i]
            if len(common) == l:
                break
            i += 1
        return common