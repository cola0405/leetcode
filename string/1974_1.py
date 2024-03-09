class Solution:
    def minTimeToType(self, word: str) -> int:
        cur = 'a'
        ans = 0
        for letter in word:
            t1 = abs(ord(letter) - ord(cur)) + 1
            t2 = 26 - abs(ord(letter) - ord(cur)) + 1
            ans += min(t1, t2)
            cur = letter
        return ans

print(Solution().minTimeToType("bza"))


