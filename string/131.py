from typing import List
class Solution:
    ans = []

    def is_palindrome(self, s):
        for i in range(len(s)//2):
            if s[i] != s[-i-1]:
                return False
        return True


    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1:
            return [[s]]

        res = []
        cur = ''
        for i in range(len(s)):
            cur += s[i]
            if self.is_palindrome(cur):
                if len(cur)==len(s):
                    res.append([cur])
                    continue

                for seq in self.partition(s[i+1:]):
                    seq.insert(0, cur)
                    res.append(seq)
        return res

print(Solution().partition("aa"))
