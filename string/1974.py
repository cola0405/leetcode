class Solution:
    def minTimeToType(self, word: str) -> int:
        cur = 'a'
        ans = 0
        for letter in word:
            if letter == cur:
                ans += 1
            else:
                gap = ord(letter) - ord(cur)
                if gap>0:
                    clockwise = gap
                    anticlockwise = ((ord(cur)-ord('a')) + (ord('z')-ord(letter)) + 1)
                else:
                    clockwise = ((ord('z')-ord(cur)) + (ord(letter)-ord('a')) + 1)
                    anticlockwise = abs(gap)
                ans += min(clockwise, anticlockwise) + 1
                cur = letter

        return ans

print(Solution().minTimeToType("bza"))


