class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''
        for ch in s:
            if '0' <= ch <= '9':
                s1 += ch
            if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
                s1 += ch.lower()
        return s1 == s1[::-1]

