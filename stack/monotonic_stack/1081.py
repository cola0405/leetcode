from collections import Counter
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        count = Counter(s)
        for ch in s:
            count[ch] -= 1
            if ch in stack:  # while已经保证了最优
                continue
            while stack and stack[-1] > ch and count[stack[-1]] > 0:
                stack.pop()
            stack.append(ch)

        return ''.join(stack)

print(Solution().smallestSubsequence("bcabc"))
