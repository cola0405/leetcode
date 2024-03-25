from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [-1]*n   # default -1 means all elements from cur to left-end can contribute for rectangle
        ms = []
        for i in range(n):
            while ms and heights[i] <= heights[ms[-1]]:
                ms.pop()
            if ms:
                left[i] = ms[-1]
            ms.append(i)

        right = [n]*n   # default n means all elements from cur to right-end can contribute for rectangle
        ms = []
        for i in range(n)[::-1]:
            while ms and heights[i] <= heights[ms[-1]]:
                ms.pop()
            if ms:
                right[i] = ms[-1]
            ms.append(i)

        ans = 0
        for i in range(n):
            ans = max(ans, heights[i]*(right[i]-left[i]-1))
        return ans

print(Solution().largestRectangleArea( [2,4]))