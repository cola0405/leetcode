class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {')':'(', ']':'[', '}':'{'}
        for ch in s:
            if ch in d:
                if len(stack)>0 and stack[-1] == d[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        if len(stack) == 0:
            return True
        return False

print(Solution().isValid(s = "()[]{}"))