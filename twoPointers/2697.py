class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s1 = list(s)
        s2 = list(s[::-1])
        for i in range(len(s1)):
            if s1[i] < s2[i]:
                s1[-i-1] = s1[i]
            elif s1[i] > s2[i]:
                s1[i] = s2[i]
        return ''.join(s1)
