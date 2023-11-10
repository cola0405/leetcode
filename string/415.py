class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = list(num1)
        num2 = list(num2)

        n, m = len(num1), len(num2)

        ans = []
        i = -1
        carry = 0
        while i>=-n and i>=-m:
            digit = int(num1[i])+int(num2[i]) + carry
            ans.append(str(digit%10))
            carry = digit // 10
            i -= 1

        while i>=-n:
            digit = int(num1[i])+carry
            ans.append(str(digit%10))
            carry = digit//10
            i -= 1

        while i>=-m:
            digit = int(num2[i]) + carry
            ans.append(str(digit % 10))
            carry = digit // 10
            i -= 1

        if carry != 0:
            ans.append('1')
        return ''.join(ans[::-1])

print(Solution().addStrings(num1 = "6994", num2 = "36"))

