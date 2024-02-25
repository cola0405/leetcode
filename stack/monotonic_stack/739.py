from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures))[::-1]:
            while len(stack)>0 and temperatures[stack[-1]]<temperatures[i]:
                stack.pop()
            if len(stack) > 0:
                ans[i] = stack[-1] - i
            else:
                ans[i] = 0
            stack.append(i)
        return ans

print(Solution().dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73]))
