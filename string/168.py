# 每一位都需要做偏移
# 所以需要放在while循环里

# ps：是做偏移，不是损失

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ''
        alpha = [chr(i) for i in range(65, 91)]
        while columnNumber > 0:
            columnNumber -= 1  # 偏移操作
            ans = alpha[columnNumber%26] + ans
            columnNumber //= 26
        return ans

print(Solution().convertToTitle(1))