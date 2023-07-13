# 检查的时间复杂度O(log num)
# 这个是双重循环时间复杂度是O(nlogn) 的例子
# 但是对于10^9 还是不够看。。 当首位数字是9的时候就很难顶了

# 尝试用二分优化到O(log^2n) -- 不行。。 因为符合的目标是离散的。。。不支持二分
# 那说明还得找分析找贪心策略 -- 勤写测试用例

# 945222221
# 742222228
# 勤写测试用例，不难发现有下降，则需要(-1 99)
# 332 (-1 99)后新的下降出现 -- 需要找到最左再(-1 99)


class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(str(n))
        for i in range(len(digits)-1):
            if digits[i] > digits[i+1]:
                # 找到最左的再(-1 99) 避免新的下降出现
                while i-1 >=0 and digits[i] == digits[i-1]:
                    i -= 1
                digits[i] = chr(ord(digits[i])-1)
                for j in range(i+1, len(digits)):
                    digits[j] = '9'
                return int(''.join(digits))
        return int(''.join(digits))


print(Solution().monotoneIncreasingDigits(332))