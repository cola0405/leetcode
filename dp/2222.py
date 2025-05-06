class Solution:
    def numberOfWays(self, s: str) -> int:
        one = 0
        zero = 0
        cnt_01 = 0
        cnt_10 = 0
        ans = 0
        for c in s:
            if c == '1':
                ans += cnt_10
                one += 1
                cnt_01 += zero
            else:
                ans += cnt_01
                zero += 1
                cnt_10 += one
        return ans