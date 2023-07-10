# 两边走 108ms
# 暴力 468ms
class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                t = s[i:j]
                if t == t[::-1]:
                    ans += 1

        return ans

s = Solution()
print(s.countSubstrings('abc'))