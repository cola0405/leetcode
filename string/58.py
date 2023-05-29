class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        i = len(s)-1
        while i>=0:
            if s[i] == " ":
                return len(s)-1-i
            i -= 1
        return len(s)

print(Solution().lengthOfLastWord(s = "   fly me   to   the moon  "))