class Solution:
    def calculate(self, s: str) -> int:
        def deal_previous(num):
            if len(op) > 0:
                if op[-1] == '*':
                    nums[-1] *= num
                    op.pop()
                elif op[-1] == '/':
                    nums[-1] //= num
                    op.pop()
                else:
                    nums.append(num)
            else:
                nums.append(num)  # when init

        nums = []
        op = []
        num = 0
        for ch in s:
            if ch.isnumeric():
                num = num*10 + int(ch)
            elif ch != ' ':
                deal_previous(num)
                num = 0
                op.append(ch)
        deal_previous(num)

        if len(nums) == 0:
            return 0

        # eval stack
        ans = nums[0]
        i = 1
        for item in op:
            if item == '+':
                ans += nums[i]
            elif item == '-':
                ans -= nums[i]
            i += 1
        return ans

print(Solution().calculate("2*3+4"))