class Solution:
    def minimumSum(self, num: int) -> int:
        digits = []
        for i in range(4):
            digits.append(num%10)
            num //= 10

        digits.sort()
        num1 = 0
        num2 = 0
        for digit in digits:
            if num1 > num2:
                num2 = num2*10+digit
            else:
                num1 = num1*10+digit
        return num1+num2

print(Solution().minimumSum(num = 4009))

