class Solution:
    def calculate(self, s: str) -> int:
        nums = []
        pre_sign = ''
        num = 0
        for i in range(len(s)):
            if s[i].isnumeric():
                num = num*10 + int(s[i])
            if s[i] in '+-*/' or i == len(s)-1:
                if pre_sign == '*':
                    nums[-1] *= num
                elif pre_sign == '/':
                    nums[-1] = int(nums[-1]/num)  # -3//2=-2 原则是向下取整
                elif pre_sign == '+':
                    nums.append(num)
                elif pre_sign == '-':
                    nums.append(-num)
                else:   # for init empty nums
                    nums.append(num)
                num = 0
                pre_sign = s[i]
        return sum(nums)

print(Solution().calculate("14-3/2"))