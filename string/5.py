# 中心扩散解决回文串问题
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = s[0]
        for i in range(len(s)-1):
            # odd
            left = i
            right = i
            while left>=0 and right<len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            ps = s[left+1: right]
            if len(ps) > len(ans):
                ans = ps

            # even
            left = i
            right = i+1
            while left>=0 and right<len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            ps = s[left+1: right]
            if len(ps) > len(ans):
                ans = ps
        return ans

print(Solution().longestPalindrome("ccc"))
