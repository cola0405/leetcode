# 草稿纸不难发现，贪心策略是不让大的数在左边
# 即遇到i>i+1，则删除
# 再这种处理过程吻合stack（不要直接pop，stack对pop有优化）

# 之后别忘了首尾的数据处理
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        from collections import deque
        stack = deque()
        for the_num in num:
            while k>0 and len(stack)>0 and the_num < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(the_num)
        while k>0:
            stack.pop()
            k -= 1
        while len(stack)>1 and stack[0]=='0':
            stack.popleft()
        if len(stack) == 0:
            return '0'
        return ''.join(stack)

print(Solution().removeKdigits("1432219",
3))
