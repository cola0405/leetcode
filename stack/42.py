from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = []
        for i in range(len(height)):
            cur = (height[i], i)
            if len(stack) == 0 or height[i] < stack[0][0]:
                stack.append(cur)
            else:  # 找到右边有比栈底更高的板子，则说明消耗殆尽，可以立马统计
                v = (i-stack[0][1])*stack[0][0]  # 不减1是因为栈底元素在，避免多减
                while stack:
                    v -= stack.pop()[0]
                ans += v
                stack.append(cur)
        # 处理后事，从右往左，如果发现更高则消耗殆尽，立马统计
        i = 0
        while len(stack)>0:
            right = stack.pop()
            # detect to left
            v = 0
            while len(stack)>0 and stack[-1][0]<right[0]:
                v -= stack.pop()[0]
            if len(stack) == 0:
                break
            v += (right[1]-stack[-1][1]-1)*right[0]
            ans += max(v, 0)
        return ans

print(Solution().trap(height = [4,2,0,3,2,5]))

