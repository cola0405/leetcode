# greedy
class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        for i in range(len(s)//2):
            if s[i] != s[n-i-1]:
                s1 = s[:i] + s[i+1:]
                s2 = s[:n-i-1] + s[n-i:]
                if s1 == s1[::-1] or s2 == s2[::-1]:
                    return True
                return False
        return True

print(Solution().validPalindrome("eccer"))