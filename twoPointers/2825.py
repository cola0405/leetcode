class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        j = 0
        for c in str1:
            nxt = chr(ord(c)+1)
            if c == 'z':
                nxt = 'a'

            if str2[j] == c or str2[j] == nxt:
                j += 1

            if j == len(str2):
                return True
        return False