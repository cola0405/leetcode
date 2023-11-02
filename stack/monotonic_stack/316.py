class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        from collections import Counter
        count = Counter(s)
        n = len(s)
        stack = []
        for i in range(n):
            count[s[i]] -= 1
            if s[i] in stack:
                continue
            while len(stack) > 0 and s[i]<stack[-1] and count[stack[-1]]>0:
                stack.pop()
            stack.append(s[i])
        return ''.join(stack)


print(Solution().removeDuplicateLetters(s = "cbacdcbc"))