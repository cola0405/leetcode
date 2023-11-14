class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s1 = ''
        for ch in s:
            if 'a' <= ch <= 'z' or '0' <= ch <= '9':
                s1 += ch

        for i in range(len(s1)//2):
            if s1[i] != s1[-i-1]:
                return False
        return True

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))