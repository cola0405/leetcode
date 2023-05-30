class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ch in s:
            if len(stack)>0 and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)


print(Solution().removeDuplicates("abbaca"))