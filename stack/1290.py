class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        top_count = [0]  # top连续的数量
        stack = []
        for ch in s:
            if len(stack)>0 and ch == stack[-1]:
                top_count[-1] += 1
            else:
                top_count.append(1)
            stack.append(ch)
            if ch == stack[-1] and top_count[-1] >= k:
                for i in range(k):
                    stack.pop()
                top_count.pop()
        return ''.join(stack)

print(Solution().removeDuplicates(s = "deeedbbcccbdaa", k = 3))


