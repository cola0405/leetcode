class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def update(st):
            i = 0
            st = list(st)
            for c in st:
                if c != '#':
                    st[i] = c
                    i += 1
                elif i > 0:
                    i -= 1
            return st[:i]

        return update(s) == update(t)

print(Solution().backspaceCompare(s = "ab#c", t = "ad#c"))