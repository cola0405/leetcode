class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for i in range(len(columnTitle)):
            ans *= 26
            ans += (ord(columnTitle[i]) - 65) + 1  # 偏移
        return ans
print(Solution().titleToNumber('AB'))
