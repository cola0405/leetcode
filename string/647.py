class Solution:
    def check(self, s, l, r):
        count = 0
        while l>=0 and r<len(s):
            if s[l] != s[r]:
                return count
            l -= 1
            r += 1
            count += 1
        return count

    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            # check odd
            ans += self.check(s, i, i)

            # check even
            ans += self.check(s, i, i+1)
        return ans

s = Solution()
print(s.countSubstrings('aaa'))