class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        left_count = 0
        for ch in s:
            if ch == ')' and left_count == 0:
                continue
            if ch == '(':
                left_count += 1
            elif ch == ')':
                left_count -= 1
            stack.append(ch)

        if left_count != 0:
            count = 0
            for i in range(len(stack))[::-1]:
                if stack[i] == '(':
                    stack.pop(i)
                    count += 1
                if count == left_count:
                    break
        return ''.join(stack)

print(Solution().minRemoveToMakeValid(s = "lee(t(c)o)de)"))