from functools import cache

class Solution:
    def isValid(self, s: str) -> bool:
        if s == 'abc':
            return True
        for i in range(len(s)-2):
            seg = s[i:i+3]
            if seg == 'abc':
                return self.isValid(s[:i] + s[i+3:])
        return False

print(Solution().isValid("aabcbc"))