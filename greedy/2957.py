class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        word = list(word)
        ans = 0
        for i in range(1, len(word)):
            if abs(ord(word[i]) - ord(word[i-1])) <= 1:
                ans += 1
                word[i] = chr(0)
        return ans