class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {chr(i): 0 for i in range(97,123)}
        d1 = {chr(i): 0 for i in range(65,91)}
        d.update(d1)

        for ch in s:
            d[ch] += 1

        ans = 0
        for ch in d:
            ans += d[ch]//2*2
        if len(s) > ans:
            ans += 1

        return ans



print(Solution().longestPalindrome(s = "ccc"))