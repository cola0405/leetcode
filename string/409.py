class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {chr(i): 0 for i in range(97,123)}
        d1 = {chr(i): 0 for i in range(65,91)}
        d.update(d1)

        for ch in s:
            d[ch] += 1

        even_amount = 0
        odd_flag = 0
        for ch in d:
            if d[ch]%2 == 0:
                even_amount += d[ch]
            elif d[ch] > 2:
                even_amount += d[ch]-1
                odd_flag = 1
            else:
                odd_flag = 1

        if odd_flag:
            even_amount += 1
        return even_amount



print(Solution().longestPalindrome(s = "ccc"))