class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            stack.append(ch)
            if len(stack) >= 3:
                if stack[-3] == 'a' and stack[-2] == 'b' and stack[-1] == 'c':
                    for i in range(3):
                        stack.pop()
        return len(stack) == 0


print(Solution().isValid("abccba"))