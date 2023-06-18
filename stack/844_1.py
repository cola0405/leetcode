class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def update(st):
            stack = []
            for c in st:
                if c != '#':
                    stack.append(c)
                elif len(stack) > 0:
                    stack.pop()
            return stack

        return update(s) == update(t)

print(Solution().backspaceCompare(s = "ab#c", t = "ad#c"))