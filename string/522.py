from typing import List
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_sub(a, b):
            if len(b) > len(a):
                return False
            j = 0
            n = len(b)
            for i in range(n):
                while j < len(a) and a[j] != b[i]:
                    j += 1
                if j == len(a):
                    return False
                j += 1
            return True

        ans = -1
        for k in range(len(strs)):
            # search all sub
            s = strs[k]
            for i in range(len(s)):
                for j in range(i+1, len(s)+1):
                    seg = s[i:j]
                    for p in range(len(strs)):
                        if (p != k) and is_sub(strs[p], seg):
                            break
                    else:
                        ans = max(ans, len(seg))

        return ans

print(Solution().findLUSlength(["aba","cdc","eae"]))

