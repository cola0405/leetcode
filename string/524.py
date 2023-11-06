from typing import List
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def is_sub(x):
            if len(x) > len(s):
                return False
            n = len(x)
            j = 0
            for i in range(n):
                while j < len(s) and x[i] != s[j]:
                    j += 1
                if j == len(s):
                    return False
                j += 1
            return True

        dictionary.sort()
        ans = ''
        for s1 in dictionary:
            if is_sub(s1) and len(s1) > len(ans):
                ans = s1
        return ans

print(Solution().findLongestWord(s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]))