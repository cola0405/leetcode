# 检查的时间复杂度O(log num)
# 这个是双重循环时间复杂度是O(nlogn) 的例子
# 但是对于10^9 还是不够看。。 当首位数字是9的时候就很难顶了

# 尝试用二分优化到O(log^2n) -- 不行。。 因为符合的目标是离散的。。。不支持二分
# 那说明还得找分析找贪心策略 -- 勤写测试用例



class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        num = n
        while num >= 0:
            # check
            digits = str(num)
            for i in range(len(digits)-1):
                if digits[i] > digits[i+1]:
                    break
            else:
                return num
            num -= 1

print(Solution().monotoneIncreasingDigits(963856657))