# 可行的递归模拟拿不拿，但是因为10^5 会超时
class Solution:
    def numSub(self, s: str) -> int:
        ans = 0
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == '1':
                j += 1
            n = j-i
            ans += (1+n)*n // 2
            i = j+1
        return int(ans % (1e9+7))
