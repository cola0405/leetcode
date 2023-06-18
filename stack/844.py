class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        for c in s:
            if c != '#':
                stack1.append(c)
            elif len(stack1) > 0:
                stack1.pop()

        stack2 = []
        for c in t:
            if c != '#':
                stack2.append(c)
            elif len(stack2) > 0:
                stack2.pop()

        return stack1 == stack2

print(Solution().backspaceCompare(s = "ab#c", t = "ad#c"))